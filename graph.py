from langgraph.graph import StateGraph, END
from nodes.scenario import scenario_analysis
from nodes.confidence import confidence_scoring
from memory.store import load_memory
from state import ResearchState
from nodes.memory_update import memory_update
from nodes.intent import intent_classifier
from nodes.quick_flow import quick_fetcher, quick_synthesis
from nodes.deep_flow import memory_injection
from nodes.analysis import financial_analysis, risk_analysis
from nodes.validation import contradiction_detector, thesis_generator
from nodes.report import final_report
from nodes.peer_benchmark import peer_benchmark

def build_graph(query: str):
    graph = StateGraph(ResearchState)

    graph.add_node("Intent", lambda s: intent_classifier(s, query))
    graph.add_node("QuickFetch", lambda s: quick_fetcher(s, query))
    graph.add_node("QuickSynth", quick_synthesis)
    graph.add_node("MemoryUpdate", memory_update)
    graph.add_node("Memory", memory_injection)
    graph.add_node("Financials", financial_analysis)
    graph.add_node("Risks", risk_analysis)
    graph.add_node("Contradictions", contradiction_detector)
    graph.add_node("Thesis", thesis_generator)
    graph.add_node("Scenario", scenario_analysis)
    graph.add_node("Confidence", confidence_scoring)
    graph.add_node("Report", final_report)
    graph.add_node("PeerBenchmark", peer_benchmark)

    graph.set_entry_point("Intent")

    graph.add_conditional_edges(
        "Intent",
        lambda s: s["mode"],
        {
            "quick": "QuickFetch",
            "deep": "Memory"
        }
    )

    graph.add_edge("QuickFetch", "QuickSynth")
    graph.add_edge("QuickSynth", "Report")
    graph.add_edge("Memory", "Financials")
    graph.add_edge("Memory", "Risks")
    graph.add_edge("Financials", "PeerBenchmark")
    graph.add_edge("PeerBenchmark", "Thesis")
    graph.add_edge("Financials", "Contradictions")
    graph.add_edge("Risks", "Contradictions")
    graph.add_edge("Risks", "Scenario")
    graph.add_edge("Scenario", "Contradictions")
    graph.add_edge("Contradictions", "Thesis")
    graph.add_edge("Contradictions", "Confidence")
    graph.add_edge("Confidence", "Report")  
    graph.add_edge("Confidence", "MemoryUpdate")
    graph.add_edge("MemoryUpdate", "Report")
    graph.add_edge("Thesis", "Report")
    graph.add_edge("Report", END)

    return graph.compile()
