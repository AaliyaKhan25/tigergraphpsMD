import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables before running agent

from agent.fraud_agent import FraudInvestigationAgent

def run_benchmark():
    # ... rest of benchmark_runner.py ...
    agent_app = FraudInvestigationAgent().build_workflow()
    
    # 20 Benchmark case transaction IDs
    benchmark_cases = [f"TX_BENCHMARK_{1001 + i}" for i in range(20)]
    results = []

    print(f"Starting processing for {len(benchmark_cases)} benchmark cases...")

    for idx, tx_id in enumerate(benchmark_cases):
        initial_state = {
            "case_id": f"CASE_{tx_id}",
            "transaction_id": tx_id,
            "trigger_reason": "MODEL_HIGH_RISK_SCORE",
            "risk_score": 0.82 if idx % 2 == 0 else 0.45
        }
        
        final_state = agent_app.invoke(initial_state)
        
        output_entry = {
            "case_id": final_state["case_id"],
            "transaction_id": final_state["transaction_id"],
            "internal_investigation_record": {
                "trigger": final_state["trigger_reason"],
                "evidence_gathered": final_state["graph_evidence"],
                "policy_context": final_state["policy_rules"],
                "uncertainty_score": final_state["uncertainty_score"]
            },
            "next_best_action": {
                "before_additional_evidence": final_state["action_before_evidence"],
                "additional_evidence_received": final_state.get("additional_evidence_received", {}),
                "after_additional_evidence": final_state["action_after_evidence"]
            },
            "suspicious_activity_report": {
                "sar_required": final_state["sar_required"],
                "sar_narrative": final_state["sar_report"]
            }
        }
        results.append(output_entry)

    os.makedirs("submission", exist_ok=True)
    with open("submission/benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Benchmarking completed! Results saved to submission/benchmark_results.json")

if __name__ == "__main__":
    run_benchmark()