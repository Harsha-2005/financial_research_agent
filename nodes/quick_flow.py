def quick_fetcher(state, query: str):
    return {
        "financials": {
            "revenue_yoy": "10%",
            "margin": "22%"
        }
    }

def quick_synthesis(state):
    return {
        "insights": {
            "summary": "Revenue grew 10% YoY driven by core operations."
        },
        "confidence_scores": {
            "summary": 0.85
        }
    }
