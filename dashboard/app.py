import json
import time
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="HHGOA | Apex Graph Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# HHGOA Ultra-Dark Enterprise Styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* Main Background & Grid */
    .stApp {
        background-color: #050811;
        background-image: 
            radial-gradient(at 0% 0%, rgba(16, 185, 129, 0.08) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(59, 130, 246, 0.08) 0px, transparent 50%);
        color: #f1f5f9;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* HHGOA Header Styling */
    .hhgoa-badge {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: #000000;
        font-weight: 800;
        font-size: 0.75rem;
        padding: 4px 12px;
        border-radius: 20px;
        letter-spacing: 1.5px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 900;
        letter-spacing: -0.5px;
        background: linear-gradient(180deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
    }
    .sub-title {
        color: #64748b;
        font-size: 0.95rem;
        margin-bottom: 30px;
    }

    /* Glassmorphism Metric Cards */
    .metric-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-top: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 14px;
        padding: 20px;
        text-align: left;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
    }
    .metric-label {
        font-size: 0.75rem;
        color: #64748b;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: #38bdf8;
        margin-top: 4px;
    }

    /* Terminal Feed Container */
    .terminal-box {
        background: #020617;
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 12px;
        padding: 16px;
        font-family: 'JetBrains Mono', 'Fira Code', monospace;
        font-size: 0.82rem;
        color: #34d399;
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.8);
    }

    /* Sidebar Overrides */
    [data-testid="stSidebar"] {
        background-color: #030712;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HHGOA Header Section
# ---------------------------------------------------------
st.markdown(
    '<div class="hhgoa-badge">HHGOA OPERATIONAL PROTOCOL</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="main-title">APEX GRAPH INTELLIGENCE</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-title">Multi-Hop Fraud Syndicate Detection & Regulatory'
    ' Compliance Engine</div>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------
st.sidebar.markdown("## 🛡️ HHGOA Controls")
st.sidebar.markdown("---")

selected_case = st.sidebar.selectbox(
    "Select Target Case", [f"HHG-{i:03d}" for i in range(1, 21)]
)

uncertainty_threshold = st.sidebar.slider(
    "Risk Uncertainty Threshold", 0.0, 1.0, 0.68
)
simulated_status = st.sidebar.radio(
    "Step-Up Auth Simulation", ["FAILED", "PASSED", "TIMEOUT"]
)

search_term = st.sidebar.text_input(
    "🔍 Entity Resolution Search", placeholder="e.g. 192.168.7.23 or DEV_9999"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📄 FinCEN Deliverables")
sar_download = st.sidebar.download_button(
    label="Download SAR Report (.json)",
    data=json.dumps(
        {
            "case_id": selected_case,
            "system": "HHGOA-ApexGraph",
            "status": "FLAGGED",
            "uncertainty_score": uncertainty_threshold,
            "action": simulated_status,
        },
        indent=2,
    ),
    file_name=f"{selected_case}_FinCEN_SAR.json",
    mime="application/json",
)

# ---------------------------------------------------------
# Metric Summary Cards
# ---------------------------------------------------------
m1, m2, m3, m4 = st.columns(4)

with m1:
  st.markdown(
      f'<div class="metric-card"><div class="metric-label">Target Case</div><div'
      f' class="metric-value" style="color: #10b981;">{selected_case}</div></div>',
      unsafe_allow_html=True,
  )

with m2:
  st.markdown(
      '<div class="metric-card"><div class="metric-label">Graph Risk'
      f' Score</div><div class="metric-value">{uncertainty_threshold:.2f}</div></div>',
      unsafe_allow_html=True,
  )

with m3:
  st.markdown(
      '<div class="metric-card"><div class="metric-label">TigerGraph'
      ' Traversal</div><div class="metric-value" style="color:'
      ' #38bdf8;">3-Hop</div></div>',
      unsafe_allow_html=True,
  )

with m4:
  risk_color = (
      "#f43f5e"
      if simulated_status == "FAILED" or uncertainty_threshold > 0.70
      else "#10b981"
  )
  st.markdown(
      f'<div class="metric-card"><div class="metric-label">Action Status</div><div'
      f' class="metric-value" style="color:{risk_color}">{simulated_status}</div></div>',
      unsafe_allow_html=True,
  )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Main Workspace: PyVis Graph + LangGraph Terminal
# ---------------------------------------------------------
col_graph, col_terminal = st.columns([2, 1])

with col_graph:
  st.subheader("🕸️ TigerGraph Multi-Hop Topology Visualizer")

  # PyVis Network Visualizer Setup
  net = Network(
      height="460px", width="100%", bgcolor="#020617", font_color="#f1f5f9"
  )

  # Node definitions matching HHGOA color palette
  nodes = [
      (
          "TX_BENCHMARK",
          f"Target TX\n({selected_case})",
          "#f59e0b",
          "star",
          32,
      ),  # Amber
      ("IP_SHARED", "Proxy Subnet\n192.168.7.23", "#38bdf8", "dot", 20),  # Cyan
      (
          "DEV_FP",
          "Device Fingerprint\nDEV_9999",
          "#10b981",
          "triangle",
          20,
      ),  # Emerald
      (
          "MERCHANT",
          "Flagged Entity\nMERCHANT_28",
          "#f43f5e",
          "diamond",
          24,
      ),  # Rose
      (
          "ACCT_2",
          "Linked Account\nUSR_8821",
          "#a855f7",
          "dot",
          18,
      ),  # Purple
  ]

  for node_id, label, color, shape, size in nodes:
    if search_term and search_term.lower() in label.lower():
      color = "#facc15"  # Neon yellow highlight on match
      size += 12
    net.add_node(
        node_id, label=label, color=color, shape=shape, size=size
    )

  net.add_edge("TX_BENCHMARK", "IP_SHARED", title="ORIGIN_IP") #type:ignore
  net.add_edge("TX_BENCHMARK", "DEV_FP", title="DEVICE_USED") #type:ignore
  net.add_edge("TX_BENCHMARK", "MERCHANT", title="PROCESSED_AT") #type:ignore
  net.add_edge("IP_SHARED", "ACCT_2", title="SHARED_INFRA") #type:ignore

  net.barnes_hut()
  net.save_graph("hhgoa_graph.html")

  with open("hhgoa_graph.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=480)

with col_terminal:
  st.subheader("⚡ LangGraph Execution Stream")

  with st.status("🤖 Executing Reasoning Pipeline...", expanded=True) as status:
    st.write("🔍 **GSQL Node:** Traversed 3 hops in TigerGraph.")
    st.write(f"🛡️ **Policy Node:** Calculated uncertainty = {uncertainty_threshold}.")
    st.write("📲 **Step-Up Auth:** Dispatched MFA challenge.")

    if simulated_status == "FAILED":
      st.write("🚨 **Lockdown Node:** MFA challenge FAILED.")
      status.update(
          label="🚨 Account Frozen & SAR Filed",
          state="error",
          expanded=True,
      )
    else:
      st.write("✅ **Clearance Node:** MFA challenge PASSED.")
      status.update(
          label="✅ Transaction Cleared", state="complete", expanded=True
      )

  st.subheader("📝 Compliance Officer Audit")
  audit_note = st.text_area(
      "HHGOA Investigation Notes",
      placeholder="Type audit trail comments here...",
      height=90,
  )
  if st.button("Persist to TigerGraph Memory"):
    st.toast("Decision successfully persisted to TigerGraph memory!", icon="💾")

# ---------------------------------------------------------
# HHGOA Code Inspector & Export Modules
# ---------------------------------------------------------
with st.expander("🐅 Inspect TigerGraph GSQL Pattern Query"):
  st.code(
      f"""
// HHGOA Multi-Hop Graph Traversal Pattern Query
INTERPRET QUERY (STRING target_id) FOR GRAPH FraudGraph {{
    Start = {{Target_Tx.*}};
    
    // Hop 1: Retrieve IP and Device Fingerprint Subgraphs
    Hop1 = SELECT t FROM Start:s -(ORIGIN_IP|DEVICE_USED:e)- :t 
           WHERE s.id == "{selected_case}";
           
    // Hop 2: Identify secondary compromised accounts over shared infrastructure
    Hop2 = SELECT a FROM Hop1:h -(SHARED_INFRA:e)- Account:a
           WHERE a.risk_rating > {uncertainty_threshold};

    PRINT Hop1, Hop2;
}}
    """,
      language="sql",
  )

with st.expander("📊 Export Graph Evidence CSV"):
  evidence_df = pd.DataFrame([
      {
          "Case ID": selected_case,
          "Relation": "ORIGIN_IP",
          "Connected Entity": "192.168.7.23",
          "Risk Rating": 0.82,
      },
      {
          "Case ID": selected_case,
          "Relation": "DEVICE_USED",
          "Connected Entity": "DEV_9999",
          "Risk Rating": 0.91,
      },
      {
          "Case ID": selected_case,
          "Relation": "PROCESSED_AT",
          "Connected Entity": "MERCHANT_28",
          "Risk Rating": 0.95,
      },
      {
          "Case ID": "192.168.7.23",
          "Relation": "SHARED_INFRA",
          "Connected Entity": "USR_8821",
          "Risk Rating": 0.74,
      },
  ])

  st.dataframe(evidence_df, use_container_width=True)

  st.download_button(
      label="📥 Export Evidence Table (.csv)",
      data=evidence_df.to_csv(index=False),
      file_name=f"{selected_case}_evidence_graph.csv",
      mime="text/csv",
  )