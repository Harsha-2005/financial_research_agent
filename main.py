from memory.store import load_memory
from dotenv import load_dotenv
load_dotenv()

from graph import build_graph

query = "Compare Tesla with Ford and GM"

graph = build_graph(query)
user_memory = load_memory()
input_state = {
    "query": "Compare Company A vs Company B on fundamentals",

    # For single-company analysis nodes
    "financials": {
        "revenue_trend": "Consistent growth over 3 years",
        "free_cash_flow": "Positive and improving",
        "operating_leverage": None
    },

    # For peer benchmarking
    "company_a": {
        "name": "Company A",
        "revenue_trend": "Consistent growth over 3 years",
        "free_cash_flow": "Positive and improving",
        "debt_to_equity": "0.4"
    },

    "company_b": {
        "name": "Company B",
        "revenue_trend": "Volatile growth",
        "free_cash_flow": "Positive but inconsistent",
        "debt_to_equity": "0.8"
    },

    "assumptions": {
        "inflation": "high",
        "growth": "slowing",
        "interest_rates": "rising"
    },

    "user_memory": user_memory
}


result = graph.invoke(input_state)
print(result["report"])
