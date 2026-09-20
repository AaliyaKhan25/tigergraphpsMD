def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        
        # Fixed: password defaults to "" to satisfy Pylance str type requirement
        self.conn = TigerGraphConnection(
            host=os.getenv("TG_HOST", "https://savanna.tgcloud.io"),
            username=os.getenv("TG_USERNAME", "tigergraph"),
            password=os.getenv("TG_PASSWORD", ""),  # <--- Changed this line
            graphname=os.getenv("TG_GRAPH", "FraudGraph")
        )