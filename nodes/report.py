def final_report(state):
    report = f"""
EXECUTIVE SUMMARY
{state.get("insights", {})}

BULL CASE
{state.get("bull_case", {})}

BEAR CASE
{state.get("bear_case", {})}

RISKS
{state.get("risks", {})}

SCENARIO & STRESS TESTING
{state.get("scenario_analysis")}

CONTRADICTIONS
{state.get("contradictions", [])}

PEER BENCHMARKING
{state.get("peer_comparison", "Not available")}

PEER TAKEAWAY
{state.get(
    "peer_takeaway",
    "Peer benchmarking could not be performed because no peer data was provided."
)}

CONFIDENCE
{state.get("confidence_scores", {})}

CONFIDENCE ASSESSMENT
{state.get("confidence")}
"""
    return {"report": report}