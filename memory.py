from collections import defaultdict

from app.agents.city_agents import (
    traffic_agent,
    weather_agent,
    emergency_agent,
    sentiment_agent
)

VOTE_WEIGHT = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3
}


def analyze_city(input_data: dict):
    """
    Central coordinator that:
    - Runs all agents
    - Applies weighted voting
    - Returns final decision
    Memory calls are skipped.
    """

    # ------------------------
    # RUN AGENTS
    # ------------------------
    agents = {
        "traffic": traffic_agent(input_data),
        "weather": weather_agent(input_data),
        "emergency": emergency_agent(input_data),
        "sentiment": sentiment_agent(input_data)
    }

    vote_pool = defaultdict(float)
    explanations = {}

    for name, result in agents.items():
        # ---- Safety guard ----
        vote = result.get("vote", "LOW")
        confidence = float(result.get("confidence", 0.5))
        reason = result.get("reason", "No explanation provided")

        weighted_vote = VOTE_WEIGHT.get(vote, 1) * confidence
        vote_pool[vote] += weighted_vote
        explanations[name] = reason

    final_vote = max(vote_pool, key=vote_pool.get)

    # ------------------------
    # ACTIONS
    # ------------------------
    if final_vote == "HIGH":
        actions = [
            "Activate emergency protocol",
            "Send public alerts",
            "Issue official communication"
        ]
    elif final_vote == "MEDIUM":
        actions = [
            "Deploy field officers",
            "Monitor situation"
        ]
    else:
        actions = ["Routine monitoring"]

    decision = {
        "final_risk_level": final_vote,
        "vote_summary": dict(vote_pool),
        "agent_votes": agents,
        "decision_explanation": explanations,
        "actions": actions
    }

    return decision
