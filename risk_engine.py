def calculate_city_risk(traffic, weather, emergency):
    score = (
        traffic.congestion_level * 0.3 +
        weather.risk_level * 0.4 +
        emergency.severity * 0.5
    )

    if score >= 7:
        return "HIGH"
    elif score >= 4:
        return "MEDIUM"
    return "LOW"
