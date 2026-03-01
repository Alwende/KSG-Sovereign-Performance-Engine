import json

def calculate_compliance(standard_days, actual_days):
    """
    Logic: If actual <= standard, compliance is 100%.
    If actual > standard, compliance is (standard/actual)*100.
    """
    if actual_days <= standard_days:
        return 100.0
    return round((standard_days / actual_days) * 100, 2)

def generate_report_entry(service_id, achievement_value):
    # This simulates pulling the standard from our schema
    standards = {
        1: {"name": "Processing of training certificates", "target": 5},
        2: {"name": "Response to consultancy enquiries", "target": 2} # 48 hours = 2 days
    }
    
    target = standards[service_id]["target"]
    compliance = calculate_compliance(target, achievement_value)
    
    entry = {
        "service": standards[service_id]["name"],
        "target_standard": f"Within {target} days",
        "actual_achievement": f"{achievement_value} days",
        "compliance": f"{compliance}%",
        "needs_ai_analysis": compliance < 100
    }
    return entry

# Simulation of a monthly reporting cycle
monthly_results = [
    generate_report_entry(1, 7), # 2 days late
    generate_report_entry(2, 1)  # Ahead of schedule
]

print(json.dumps(monthly_results, indent=2))
