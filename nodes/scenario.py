from utils.llm import call_llm

def scenario_analysis(state):
    system_prompt = """
You are a junior equity analyst performing scenario and stress testing.

Rules:
- Do NOT invent financial numbers or percentages
- Use qualitative ranges only (e.g., 'moderate', 'material')
- Use cautious, conditional language
- Tie scenarios to revenue, margins, and cash flow
"""


    assumptions = state.get("assumptions", {
        "inflation": "high",
        "growth": "slowing",
        "interest_rates": "rising"
    })

    user_prompt = f"""
Perform scenario and stress testing based on the following assumptions.
IMPORTANT: Avoid numeric estimates unless explicitly provided in the data.


Assumptions:
- Inflation: {assumptions.get("inflation")}
- Growth: {assumptions.get("growth")}
- Interest rates: {assumptions.get("interest_rates")}

Available financial context:
{state.get("financials")}

Explain:
1. Impact on revenue
2. Impact on margins
3. Impact on free cash flow
4. Overall risk profile shift

Be structured and concise.
"""

    analysis = call_llm(system_prompt, user_prompt)

    return {
        "scenario_analysis": {
            "assumptions": assumptions,
            "analysis": analysis
        }
    }
