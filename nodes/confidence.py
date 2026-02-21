def confidence_scoring(state):
    """
    Confidence is heuristic-based (not LLM-based) to avoid latency.
    """

    confidence = {}

    # Base confidence depends on data availability
    financials = state.get("financials", {})
    assumptions = state.get("assumptions", {})

    # Section-level confidence
    confidence["fundamentals"] = 0.8 if financials else 0.4
    confidence["bull_case"] = 0.75 if financials else 0.45
    confidence["bear_case"] = 0.7 if financials else 0.45
    confidence["risks"] = 0.85
    confidence["scenario"] = 0.65 if assumptions else 0.4

    # Overall confidence (simple aggregation)
    confidence["overall"] = round(
        sum(confidence.values()) / len(confidence), 2
    )

    # Explanation (human-readable)
    confidence["rationale"] = (
        "Confidence reflects data completeness and reliance on assumptions. "
        "Higher confidence in risk identification; lower confidence where "
        "scenarios rely on macro assumptions rather than reported figures."
    )

    return {"confidence": confidence}