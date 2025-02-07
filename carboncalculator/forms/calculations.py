def calculate_carbon_footprint(session_data):
    carbon_score = 0
    
    # Travel emissions (example)
    travel = session_data.get('travel', {})
    if travel:
        distance = travel.get('distance_travelled', 0)
        frequency = travel.get('frequency', 1)
        carbon_score += distance * frequency * 0.2  # Example emission factor

    # Waste emissions
    waste = session_data.get('waste', {})
    if waste:
        carbon_score += waste.get('biodegradable_waste', 0) * 0.1

    # Energy emissions
    energy = session_data.get('energy', {})
    if energy:
        carbon_score += energy.get('electricity_bill', 0) * 0.5

    return round(carbon_score, 2)
