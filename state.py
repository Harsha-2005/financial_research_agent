from typing import TypedDict, Dict, List, Optional, Any

class ResearchState(TypedDict):
    # Mode
    mode: Optional[str]  # quick | deep

    # Preferences / memory
    risk_profile: Optional[str]
    preferred_kpis: List[str]

    # Analysis data
    financials: Dict[str, Any]
    insights: Dict[str, Any]
    risks: Dict[str, Any]
    bull_case: Dict[str, Any]
    bear_case: Dict[str, Any]
    scenario_analysis: dict


    # Validation
    contradictions: List[str]
    confidence_scores: Dict[str, float]
    confidence: dict


    # Peer benchmarking (explicit peers)
    company: Optional[str]
    peers: Optional[List[str]]
    peer_comparison: Optional[Dict[str, Any]]
    peer_takeaway: Optional[str]

    # Output
    report: Optional[str]