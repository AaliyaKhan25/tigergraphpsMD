# 🐅 Apex Graph Intelligence & Autonomous Fraud Oversight

Enterprise Multi-Hop Graph Traversal • LangGraph Agentic Reasoning • FinCEN Regulatory Compliance

---

## 📌 Executive Overview

Apex Graph Intelligence is an enterprise-grade autonomous fraud detection and regulatory compliance platform designed to uncover multi-hop fraud syndicates. Traditional rules-based anti-money laundering (AML) and transaction monitoring systems evaluate transactions in isolation. Modern financial crime networks, however, operate across distributed entity layers using synthetic identities, shared proxy subnets, compromised device fingerprints, and merchant routing channels.

This system integrates TigerGraph's parallelized GSQL query engine with a LangGraph multi-agent orchestration architecture. It automatically ingests raw transaction alerts, executes deep multi-hop graph pattern matching across relational entity graphs, evaluates compliance policy risks, triggers step-up authentication challenges, and outputs FinCEN-compliant Suspicious Activity Reports (SAR).

---

## 🏗️ System Architecture

The platform operates across four decoupled layers: Data Ingestion, TigerGraph Query Engine, LangGraph Multi-Agent Runtime, and the Human-In-The-Loop (HITL) Operations Dashboard.

```text

┌────────────────────────────────────────────────────────────────────────────────────────┐

│                                 DATA INGESTION LAYER                                    │

│   [ Transaction Feeds ] ───► [ Real-Time Network Events ] ───► [ Device Fingerprints ]  │

└───────────────────────────────────┬────────────────────────────────────────────────────┘

                                    │

                                    ▼

┌────────────────────────────────────────────────────────────────────────────────────────┐

│                              TIGERGRAPH GRAPH DATABASE                                 │

│  • Entity Resolution & Schema (Account, Target_Tx, IP_Address, Device_FP, Merchant)   │

│  • Deep Multi-Hop Traversal Engine (GSQL Pattern Matching Engine)                      │

└───────────────────────────────────┬────────────────────────────────────────────────────┘

                                    │

                                    ▼

┌────────────────────────────────────────────────────────────────────────────────────────┐

│                            LANGGRAPH MULTI-AGENT ORCHESTRATION                         │

│  ┌──────────────────────┐    ┌─────────────────────────┐    ┌──────────────────────┐   │

│  │ Traversal Evaluator  │───►│ Policy & Rules Engine   │───►│ SAR Narrative Engine │   │

│  └──────────────────────┘    └─────────────────────────┘    └──────────────────────┘   │

└───────────────────────────────────┬────────────────────────────────────────────────────┘

                                    │

                                    ▼

┌────────────────────────────────────────────────────────────────────────────────────────┐

│                              HUMAN-IN-THE-LOOP (HITL) UI                               │

│  • Streamlit High-Contrast Dashboard                                                   │

│  • Topology Visualizer, Decision Timeline, & Direct GSQL Memory Persistence            │

└────────────────────────────────────────────────────────────────────────────────────────┘

````

### 🛠️ Core Capabilities & Module Breakdown

Multi-Hop Graph Topology Engine

Entity Resolution: Dynamically links disparate accounts based on shared hardware fingerprints (DEV_*), proxy subnets (IP_*), and high-risk merchant destinations (MERCHANT_*).

Network Graph Visualizer: High-contrast network topology rendering for Security Operations Centers (SOC):

🟨 Target Transaction (TARGET TX): Primary transaction under audit (e.g., TX_BENCHMARK_1001).

🟦 Shared IP Node (SHARED IP): Network connection endpoints (e.g., 192.168.7.23).

🟩 Device Fingerprint (DEVICE FP): Unique hardware identification hashes (e.g., DEV_9999).

🟪 Account Node (ACCOUNT): Originating banking account credentials (e.g., USR_6001).

🟥 High-Risk Entity (HIGH RISK MERCHANT): Blacklisted merchants or flagged receiving entities (e.g., MERCHANT_28).

### LangGraph Agent Decision Pipeline

Autonomous Step-Up Triggering: Automatically dispatches biometric or multi-factor authentication challenges when transaction uncertainty ratings exceed configured thresholds (> 0.50).

State Progression Tracking: Evaluates risk metrics dynamically before and after step-up authentication challenges.

Account Lockdown Protocol: Instantly freezes compromised accounts if step-up authentication returns a FAILED or timed-out status.

### Compliance & Policy Engine

Rules Engine Evaluation: Evaluates raw graph traversal outputs against FinCEN guidelines, BSA regulations, and risk scoring models (MODEL_HIGH_RISK_SCORE).

Human-In-The-Loop (HITL) Override: Allows compliance officers to inspect evidence graphs, submit audit notes, and persist manually approved or declined decisions back into graph memory.

### Automated FinCEN SAR Filing Generator

LLM Regulatory Narratives: Synthesizes graph evidence, transaction histories, shared infrastructure metrics, and agent audit trails into standard compliance narratives.

## 🗄️ TigerGraph Schema & Benchmark JSON Structure

### GSQL Schema Definition (gsql/schema.gsql)

CREATE VERTEX Account (PRIMARY_ID id STRING, account_created_at DATETIME, risk_rating DOUBLE)

CREATE VERTEX Target_Tx (PRIMARY_ID id STRING, amount DOUBLE, timestamp DATETIME, risk_score DOUBLE)

CREATE VERTEX IP_Address (PRIMARY_ID ip STRING, proxy_flag BOOL)

CREATE VERTEX Device_FP (PRIMARY_ID dev_id STRING, is_rooted BOOL)

CREATE VERTEX High_Risk_Merchant (PRIMARY_ID merchant_id STRING, category STRING)

CREATE DIRECTED EDGE INITIATED (FROM Account, TO Target_Tx)

CREATE DIRECTED EDGE ORIGIN_IP (FROM Target_Tx, TO IP_Address)

CREATE DIRECTED EDGE DEVICE_USED (FROM Target_Tx, TO Device_FP)

CREATE DIRECTED EDGE PROCESSED_AT (FROM Target_Tx, TO High_Risk_Merchant)

CREATE UNDIRECTED EDGE SHARED_INFRA (FROM Target_Tx, TO Target_Tx)

CREATE GRAPH FraudGraph(\*)

Benchmark Case Output Format (cases/HHG-001.json)

The evaluator expects individual JSON objects matching the schema below inside the root cases/ directory:

```json
{

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

📂 Repository Directory Structure

tigergraphpsMD/

├── cases/                        # Mandatory hackathon submission folder

│   ├── HHG-001.json              # Evaluated case output 1

│   ├── HHG-002.json              # Evaluated case output 2

│   ├── ...

│   └── HHG-020.json              # Evaluated case output 20

├── agent/

│   ├── __init__.py

│   ├── benchmark_runner.py       # Orchestrates batch graph traversals

│   ├── state.py                  # LangGraph state schema definitions

│   └── nodes.py                  # Multi-agent reasoning nodes & tool logic

├── dashboard/

│   └── app.py                    # Streamlit analytical interface

├── submission/

│   └── benchmark_results.json    # Consolidated benchmark array output (27KB)

├── case_pack.csv                 # Raw benchmark inputs

├── gsql/

│   ├── schema.gsql               # TigerGraph vertex/edge definitions

│   └── queries/                  # GSQL multi-hop pattern queries

├── .env.example                  # Environment variable template

├── .gitignore                    # Sensitive file exclusions

├── requirements.txt              # Dependency specifications

└── README.md                     # Documentation

⚙️ Setup & Execution Guide

Step 1: Initialize Virtual Environment

Clone your repository and initialize an isolated Python 3.10+ virtual environment:

```powershell
# Navigate to project directory

cd C:\Users\ASUS\tigergraphpsMD

# Create virtual environment

python -m venv venv

# Activate on Windows PowerShell

.\venv\Scripts\Activate.ps1

# Activate on macOS/Linux

# source venv/bin/activate

Step 2: Install Project Dependencies

Upgrade pip and install all required runtime dependencies:

PowerShell

python -m pip install --upgrade pip

pip install -r requirements.txt


### Step 3: Configure Environment Credentials

Copy .env.example to create your active .env file:

```powershell
copy .env.example .env

Open .env and fill in your API credentials:

Code snippet

OPENAI_API_KEY=sk-proj-your-actual-api-key-here

TG_HOST=[https\://savanna.tgcloud.io](https\://savanna.tgcloud.io)

TG_USERNAME=tigergraph

TG_PASSWORD=your_tigergraph_password_here

TG_GRAPH=FraudGraph

Step 4: Execute Agentic Benchmark Pipeline

Run the multi-agent graph traversal pipeline across the 20 benchmark cases in case_pack.csv:

python -m agent.benchmark_runner

This processes all test cases and outputs submission/benchmark_results.json.

Step 5: Generate Mandatory Cases Folder

Run this inline Python script to split submission/benchmark_results.json into the required cases/HHG-001.json through cases/HHG-020.json files:

```powershell
python -c "import json, os; os.makedirs('cases', exist_ok=True); data = json.load(open('submission/benchmark_results.json')); [json.dump(item, open(f'cases/HHG-{i+1:03d}.json', 'w'), indent=2) for i, item in enumerate(data[:20])]; print('Successfully created 20 HHG JSON files in cases/!')"

Verify the files were generated correctly:

```powershell
Get-ChildItem -Path cases

Step 6: Push Output to GitHub

Stage the generated cases, commit them, and force-push to your remote main branch:

git add cases/ submission/

git commit -m "Add required 20 HHG case JSON files in cases/ directory"

git push origin main --force
````

## 🖥️ Streamlit Analytics Dashboard Overview

The platform includes an interactive Streamlit operations dashboard (dashboard/app.py) designed for compliance analysts and security operations centers.

Launching the UI

streamlit run dashboard/app.py

Dashboard Features

Case Selector: Dropdown navigation to inspect any case from HHG-001 through HHG-020.

Interactive Topology Viewer: Visualizes multi-hop connections between accounts, transactions, proxy IPs, and device fingerprints.

Agent Decision Timeline: Real-time visual progression tracking initial triggers, step-up authentication challenges, and final risk updates.

Human-in-The-Loop Override Panel: Text fields allowing compliance analysts to submit audit notes and override agent decisions directly into graph storage.

## 🔒 Security Protocol & Push Protection

To protect API credentials and maintain compliance with GitHub Push Protection:

.env Exclusion: Ensure .env is listed inside .gitignore before making any commits.

Scrubbed Examples: Maintain .env.example with blank placeholder strings (your_api_key_here).

Commit History Cleanup: If an API key is accidentally committed, remove it from Git history using git reset or GitHub Secret Unblocking tools before pushing.
