from app.utils.coordinator import analyze_city

def simulate_city(payload: dict):
    """
    Simulation / What-if analysis
    Runs the same analysis but labels it as simulation output
    """

    base_result = analyze_city(payload)

    return {
        "mode": "simulation",
        "input": payload,
        "predicted_outcome": base_result,
        "note": "This is a what-if simulation, not a real-time action"
    }
