def peer_benchmark(state):
    insights = state.get("insights", {})

    # No explicit peers provided
    if not state.get("peers"):
        return {
            **state,
            "peer_comparison": None,
            "peer_takeaway": (
                "No explicit peer data was provided. "
                "Peer benchmarking could not be performed. "
                "To enable this section, peer company fundamentals "
                "must be supplied or fetched."
            )
        }

    # (Future) real comparison logic goes here