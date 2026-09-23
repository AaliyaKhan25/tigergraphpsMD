# 🐅 Apex Graph Intelligence & Autonomous Fraud OversightEnterprise Multi-Hop Graph Traversal •
 LangGraph Agentic Reasoning •
  FinCEN Regulatory Compliance
##  📌 Executive Overview
Apex Graph Intelligence is an enterprise-grade autonomous fraud detection and regulatory compliance platform designed to uncover multi-hop fraud syndicates. Traditional rules-based anti-money laundering (AML) and transaction monitoring systems evaluate transactions in isolation. Modern financial crime networks, however, operate across distributed entity layers using synthetic identities, shared proxy subnets, compromised device fingerprints, and merchant routing channels.This system integrates TigerGraph's parallelized GSQL query engine with a LangGraph multi-agent orchestration architecture. It automatically ingests raw transaction alerts, executes deep multi-hop graph pattern matching across relational entity graphs, evaluates compliance policy risks, triggers step-up authentication challenges, and outputs FinCEN-compliant Suspicious Activity Reports (SAR).
 ## 🏗️ System Architecture & Visual Topology
 The platform operates across four decoupled layers: Data Ingestion, TigerGraph Query Engine, LangGraph Multi-Agent Runtime, and the Human-In-The-Loop (HITL) Operations Dashboard.
  Plaintext┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 DATA INGESTION LAYER                                    │
│   [ Transaction Feeds ] ───► [ Real-Time Network Events ] ───► [ Device Fingerprints ]  │
└───────────────────────────────────┬────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              TIGERGRAPH GRAPH DATABASE                                 │
│  • Entity Resolution & Schema (Account, Target_Tx, IP_Address, Device_FP, Merchant)   │
│  • Deep Multi-Hop Traversal Engine (GSQL Pattern Matching Engine)                      │
└───────────────────────────────────┬────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                            LANGGRAPH MULTI-AGENT ORCHESTRATION                         │
│  ┌──────────────────────┐    ┌─────────────────────────┐    ┌──────────────────────┐   │
│  │ Traversal Evaluator  │───►│ Policy & Rules Engine   │───►│ SAR Narrative Engine │   │
│  └──────────────────────┘    └─────────────────────────┘    └──────────────────────┘   │
└───────────────────────────────────┬────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              HUMAN-IN-THE-LOOP (HITL) UI                               │
│  • Streamlit High-Contrast Dashboard                                                   │
│  • Topology Visualizer, Decision Timeline, & Direct GSQL Memory Persistence            │
└────────────────────────────────────────────────────────────────────────────────────────┘
🛠️ Core Capabilities & Module Breakdown1. Multi-Hop Graph Topology EngineEntity Resolution: Dynamically links disparate accounts based on shared hardware fingerprints (DEV_*), proxy subnets (IP_*), and high-risk merchant destinations (MERCHANT_*).Network Graph Visualizer: High-contrast network topology rendering for Security Operations Centers (SOC):🟨 Target Transaction (TARGET TX): Primary transaction under audit (e.g., TX_BENCHMARK_1001).🟦 Shared IP Node (SHARED IP): Network connection endpoints (e.g., 192.168.7.23).🟩 Device Fingerprint (DEVICE FP): Unique hardware identification hashes (e.g., DEV_9999).🟪 Account Node (ACCOUNT): Originating banking account credentials (e.g., USR_6001).🟥 High-Risk Entity (HIGH RISK MERCHANT): Blacklisted merchants or flagged receiving entities (e.g., MERCHANT_28).2. LangGraph Agent Decision PipelineAutonomous Step-Up Triggering: Automatically dispatches biometric or multi-factor authentication challenges when transaction uncertainty ratings exceed configured thresholds ($>0.50$).State Progression Tracking: Evaluates risk metrics dynamically before and after step-up authentication challenges.Account Lockdown Protocol: Instantly freezes compromised accounts if step-up authentication returns a FAILED or timed-out status.3. Compliance & Policy EngineRules Engine Evaluation: Evaluates raw graph traversal outputs against FinCEN guidelines, BSA regulations, and risk scoring models (MODEL_HIGH_RISK_SCORE).Human-In-The-Loop (HITL) Override: Allows compliance officers to inspect evidence graphs, submit audit notes, and persist manually approved or declined decisions back into graph memory.4. Automated FinCEN SAR Filing GeneratorLLM Regulatory Narratives: Synthesizes graph evidence, transaction histories, shared infrastructure metrics, and agent audit trails into standard compliance narratives.🗄️ TigerGraph Schema & Benchmark JSON StructureGSQL Schema Definition (gsql/schema.gsql)SQLCREATE VERTEX Account (PRIMARY_ID id STRING, account_created_at DATETIME, risk_rating DOUBLE)
CREATE VERTEX Target_Tx (PRIMARY_ID id STRING, amount DOUBLE, timestamp DATETIME, risk_score DOUBLE)
CREATE VERTEX IP_Address (PRIMARY_ID ip STRING, proxy_flag BOOL)
CREATE VERTEX Device_FP (PRIMARY_ID dev_id STRING, is_rooted BOOL)
CREATE VERTEX High_Risk_Merchant (PRIMARY_ID merchant_id STRING, category STRING)

CREATE DIRECTED EDGE INITIATED (FROM Account, TO Target_Tx)
CREATE DIRECTED EDGE ORIGIN_IP (FROM Target_Tx, TO IP_Address)
CREATE DIRECTED EDGE DEVICE_USED (FROM Target_Tx, TO Device_FP)
CREATE DIRECTED EDGE PROCESSED_AT (FROM Target_Tx, TO High_Risk_Merchant)
CREATE UNDIRECTED EDGE SHARED_INFRA (FROM Target_Tx, TO Target_Tx)

CREATE GRAPH FraudGraph(*)
Benchmark Case Output Format (cases/HHG-001.json)The evaluator expects individual JSON objects matching the schema below inside the root cases/ directory:JSON{
  "case_id": "CASE_TX_BENCHMARK_1001",
  "transaction_id": "TX_BENCHMARK_1001",
  "internal_investigation_record": {
    "trigger": "MODEL_HIGH_RISK_SCORE",
    "uncertainty_score": 0.65,
    "policy_context": "Standard Fraud Risk Ruleset Executed.",
    "evidence_gathered": {
      "connected_infrastructure": [
        {
          "ConnectedTx": [
            {
              "id": "TX_BENCHMARK_1001",
              "amount": 1250,
              "risk_score": 0.82
            }
          ]
        }
      ]
    }
  },
  "next_best_action": {
    "before_additional_evidence": {
      "action": "STEP_UP_AUTH",
      "approval_route": "AUTOMATED",
      "reasoning": "High uncertainty score requires additional verification."
    },
    "additional_evidence_received": {
      "step_up_auth_status": "FAILED",
      "updated_action": "FREEZE_ACCOUNT",
      "approval_route": "MANUAL_REVIEW",
      "reasoning": "Step-up authentication failed following high-risk trigger."
    }
  },
  "suspicious_activity_report": {
    "sar_required": true,
    "sar_narrative": "Automated SAR Narrative: Account associated with TX_BENCHMARK_1001 triggered high-risk scoring model..."
  }
}
📂 Repository Directory StructurePlaintexttigergraphpsMD/
├── cases/                        # Mandatory hackathon submission folder
│   ├── HHG-001.json              # Evaluated case output 1
│   ├── HHG-002.json              # Evaluated case output 2
│   ├── ...
│   └── HHG-020.json              # Evaluated case output 20
├── agent/
│   ├── __init__.py
│   ├── benchmark_runner.py       # Orchestrates batch graph traversals
│   ├── state.py                  # LangGraph state schema definitions
│   └── nodes.py                  # Multi-agent reasoning nodes & tool logic
├── dashboard/
│   └── app.py                    # Streamlit analytical interface
├── submission/
│   └── benchmark_results.json    # Consolidated benchmark array output (27KB)
├── case_pack.csv                 # Raw benchmark inputs
├── gsql/
│   ├── schema.gsql               # TigerGraph vertex/edge definitions
│   └── queries/                  # GSQL multi-hop pattern queries
├── .env.example                  # Environment variable template
├── .gitignore                    # Sensitive file exclusions
├── requirements.txt              # Dependency specifications
└── README.md                     # Documentation
⚙️ Complete Setup & Execution RunbookFollow these sequential steps to set up the environment, run the evaluation pipeline, format the required submission files, and push to GitHub.1.Initialize Virtual Environment:PowerShell / Terminal Setup.Clone your repository and initialize a isolated Python 3.10+ virtual environment:PowerShell# Navigate to project directory
cd C:\Users\ASUS\tigergraphpsMD

### Create virtual environment
python -m venv venv

### Activate on Windows PowerShell
.\venv\Scripts\Activate.ps1

## Activate on macOS/Linux
### source venv/bin/activate
2.Install Project Dependencies:Package Management.Upgrade pip and install all required runtime dependencies:PowerShellpython -m pip install --upgrade pip
pip install -r requirements.txt
3.Configure Environment Credentials:Secret Management.Copy .env.example to create your active .env file:PowerShellcopy .env.example .env
Open .env and fill in your API credentials:envOPENAI_API_KEY=sk-proj-your-actual-api-key-here
TG_HOST=https://savanna.tgcloud.io
TG_USERNAME=tigergraph
TG_PASSWORD=your_tigergraph_password_here
TG_GRAPH=FraudGraph
4.Execute Agentic Benchmark Pipeline:Batch Execution.Run the multi-agent graph traversal pipeline across the 20 benchmark cases in case_pack.csv:PowerShellpython -m agent.benchmark_runner
This processes all test cases and outputs submission/benchmark_results.json.5.Generate Mandatory Cases Folder:Data Formatting.Run this inline Python script to split submission/benchmark_results.json into the required cases/HHG-001.json through cases/HHG-020.json files:PowerShellpython -c "import json, os; os.makedirs('cases', exist_ok=True); data = json.load(open('submission/benchmark_results.json')); [json.dump(item, open(f'cases/HHG-{i+1:03d}.json', 'w'), indent=2) for i, item in enumerate(data[:20])]; print('Successfully created 20 HHG JSON files in cases/!')"
Verify the files were generated correctly:PowerShellGet-ChildItem -Path cases
6.Push Output to GitHub:Version Control.Stage the generated cases, commit them, and force-push to your remote main branch:PowerShellgit add cases/ submission/
git commit -m "Add required 20 HHG case JSON files in cases/ directory"
git push origin main --force
## 🖥️ Streamlit Analytics Dashboard OverviewThe platform includes an interactive Streamlit operations dashboard (dashboard/app.py) designed for compliance analysts and security operations centers.Launching the UIPowerShellstreamlit run dashboard/app.py
Dashboard FeaturesCase Selector: Dropdown navigation to inspect any case from HHG-001 through HHG-020.Interactive Topology Viewer: Visualizes multi-hop connections between accounts, transactions, proxy IPs, and device fingerprints.Agent Decision Timeline: Real-time visual progression tracking initial triggers, step-up authentication challenges, and final risk updates.Human-in-the-Loop Override Panel: Text fields allowing compliance analysts to submit audit notes and override agent decisions directly into graph storage.
## 🔒 Security Protocol & Push Protection
To protect API credentials and maintain compliance with GitHub Push Protection:.env Exclusion: Ensure .env is listed inside .gitignore before making any commits.Scrubbed Examples: Maintain .env.example with blank placeholder strings (your_api_key_here).Commit History Cleanup: If an API key is accidentally committed, remove it from Git history using git reset or GitHub Secret Unblocking tools before pushing.