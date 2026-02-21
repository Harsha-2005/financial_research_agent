from utils.llm import call_llm


def contradiction_detector(state):
    system_prompt = "You are an analyst checking for inconsistencies."

    user_prompt = f"""
Review the following analysis and risks.

Insights:
{state.get("insights", {})}

Risks:
{state.get("risks", {})}

Identify any contradictions or tensions between performance and risks.
If none, say 'No major contradictions'.
"""

    contradictions = call_llm(system_prompt, user_prompt)

    return {
        "contradictions": [contradictions]
    }

def thesis_generator(state):
    system_prompt = "You are an investment strategy consultant."

    # -------- BULL CASE PROMPT --------
    bull_prompt = f"""
Based on the analysis below, generate ONLY the BULL CASE.
Focus on upside drivers and positive scenarios.
Do not mention risks.

Analysis:
{state.get("insights")}
"""

    bull_response = call_llm(system_prompt, bull_prompt)

    # -------- BEAR CASE PROMPT --------
    bear_prompt = f"""
Based on the analysis below, generate ONLY the BEAR CASE.
Focus on downside risks and negative scenarios.
Do not mention upside.

Analysis:
{state.get("insights")}
Risks:
{state.get("risks")}
"""

    bear_response = call_llm(system_prompt, bear_prompt)

    return {
        "bull_case": {"analysis": bull_response},
        "bear_case": {"analysis": bear_response}
    }

