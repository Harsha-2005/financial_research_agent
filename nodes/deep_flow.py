def memory_injection(state):
    return {
        "preferred_kpis": state.get("preferred_kpis", ["FCF", "ROE"]),
        "risk_profile": state.get("risk_profile", "balanced")
    }
