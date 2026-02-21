def intent_classifier(state, query: str):
    q = query.lower()

    if any(k in q for k in ["compare", "benchmark", "vs", "versus"]):
        return {"mode": "deep"}

    if any(k in q for k in ["bull", "bear", "scenario", "risk"]):
        return {"mode": "deep"}

    return {"mode": "quick"}