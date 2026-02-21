from utils.llm import call_llm

def financial_analysis(state):
    system_prompt = """You are a junior equity analyst.IMPORTANT RULES:- Do NOT invent company names, numbers, or facts- If data is missing, explicitly say \"Data not provided\"- Base analysis ONLY on the input given- Use cautious analyst language
    User Preferences (if available):
- Risk tolerance: {state.get("user_memory", {}).get("risk_tolerance")}
- Preferred KPIs: {state.get("user_memory", {}).get("preferred_kpis")}
- Sectors of interest: {state.get("user_memory", {}).get("sectors")}
- Geographies: {state.get("user_memory", {}).get("geographies")}"""

    user_prompt = f"""
Analyze the following financial information.

If information is missing, clearly state what is missing.
Do not create hypothetical examples.

Data:
{state.get("financials", {})}

Focus on:
- Revenue trend
- Free cash flow
- Operating leverage

"""

    analysis = call_llm(system_prompt, user_prompt)

    return {
        "insights": {
            "financial_analysis": analysis
        }
    }


def risk_analysis(state):
    system_prompt = "You are a risk-focused equity analyst."

    user_prompt = f"""
Identify risks for this company.

Insights:
{state.get("insights", {})}

Separate clearly:
1. Reported risks
2. Overlooked risks
"""

    risks = call_llm(system_prompt, user_prompt)

    return {
        "risks": {
            "analysis": risks
        }
    }
