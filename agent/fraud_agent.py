import os
import json
from typing import TypedDict, Dict, Any, List
from dotenv import load_dotenv  # 1. Import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from pyTigerGraph import TigerGraphConnection


load_dotenv()

class FraudCaseState(TypedDict):
    case_id: str
    transaction_id: str
    trigger_reason: str
    risk_score: float
    graph_evidence: Dict[str, Any]
    policy_rules: str
    similar_cases: List[Dict[str, Any]]
    uncertainty_score: float
    additional_evidence_received: Dict[str, Any]
    action_before_evidence: Dict[str, Any]
    action_after_evidence: Dict[str, Any]
    approval_route: str
    sar_required: bool
    sar_report: str
    investigation_status: str

class FraudInvestigationAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.conn = TigerGraphConnection(
            host=os.getenv("TG_HOST", "https://savanna.tgcloud.io/groups/386e90dd-d805-479b-bccf-ecaf738a853b"),
            username=os.getenv("TG_USERNAME", "aaliyak"),
            password=os.getenv("TG_PASSWORD", ""),
            graphname=os.getenv("TG_GRAPH", "FraudGraph")
        )

    def trigger_node(self, state: FraudCaseState) -> FraudCaseState:
        state["investigation_status"] = "INITIALIZED"
        return state

    def investigate_graph_node(self, state: FraudCaseState) -> FraudCaseState:
        # Traverses local subgraphs & historical patterns
        tx_id = state["transaction_id"]
        try:
            results = self.conn.runInstalledQuery("detect_shared_infra", {"tx_id": tx_id})
        except Exception:
            results = [{"ConnectedTx": [{"id": tx_id, "amount": 1250.0, "risk_score": state["risk_score"]}]}]
        
        state["graph_evidence"] = {"connected_infrastructure": results}
        state["similar_cases"] = [{"case_id": "CASE_9901", "outcome": "CONFIRMED_FRAUD", "pattern": "SHARED_DEVICE"}]
        return state

    def policy_rag_node(self, state: FraudCaseState) -> FraudCaseState:
        # Match policies based on evidence
        state["policy_rules"] = (
            "Policy Rule 4.2: Transactions over $1000 with shared IP address and "
            "risk score > 0.7 require step-up authentication before blocking."
        )
        return state

    def assess_uncertainty_node(self, state: FraudCaseState) -> FraudCaseState:
        # Calculates risk and determines if step-up auth / extra evidence is needed
        if state["risk_score"] > 0.8:
            state["uncertainty_score"] = 0.65
            state["action_before_evidence"] = {
                "action": "REQUEST_STEP_UP_AUTH",
                "approval_route": "AUTOMATED",
                "reasoning": "High model risk score with ambiguous device history."
            }
        else:
            state["uncertainty_score"] = 0.15
            state["action_before_evidence"] = {
                "action": "ALLOW",
                "approval_route": "AUTOMATED",
                "reasoning": "Low risk profile and verified device."
            }
        return state

    def gather_evidence_node(self, state: FraudCaseState) -> FraudCaseState:
        # Simulates step-up authentication outcome
        state["additional_evidence_received"] = {
            "step_up_auth_status": "FAILED",
            "mfa_method": "SMS_OTP",
            "geo_mismatch_detected": True
        }
        return state

    def final_decision_node(self, state: FraudCaseState) -> FraudCaseState:
        if state.get("additional_evidence_received", {}).get("step_up_auth_status") == "FAILED":
            state["action_after_evidence"] = {
                "action": "BLOCK_ACCOUNT_AND_FREEZE",
                "approval_route": "HUMAN_ANALYST",
                "reasoning": "Failed step-up MFA challenge combined with shared IP infrastructure."
            }
            state["sar_required"] = True
            state["sar_report"] = f"Suspicious activity report for Case {state['case_id']}: Shared device cluster with failed MFA verification."
        else:
            state["action_after_evidence"] = state["action_before_evidence"]
            state["sar_required"] = False
            state["sar_report"] = ""
            
        state["investigation_status"] = "CLOSED"
        return state

    def build_workflow(self):
        builder = StateGraph(FraudCaseState)
        builder.add_node("Trigger", self.trigger_node)
        builder.add_node("InvestigateGraph", self.investigate_graph_node)
        builder.add_node("PolicyRAG", self.policy_rag_node)
        builder.add_node("AssessUncertainty", self.assess_uncertainty_node)
        builder.add_node("GatherEvidence", self.gather_evidence_node)
        builder.add_node("FinalDecision", self.final_decision_node)

        builder.set_entry_point("Trigger")
        builder.add_edge("Trigger", "InvestigateGraph")
        builder.add_edge("InvestigateGraph", "PolicyRAG")
        builder.add_edge("PolicyRAG", "AssessUncertainty")

        def route_evidence(state: FraudCaseState):
            if state["uncertainty_score"] > 0.4 and "additional_evidence_received" not in state:
                return "GatherEvidence"
            return "FinalDecision"

        builder.add_conditional_edges("AssessUncertainty", route_evidence)
        builder.add_edge("GatherEvidence", "FinalDecision")
        builder.add_edge("FinalDecision", END)

        return builder.compile()