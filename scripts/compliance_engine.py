import json

def get_ksg_ai_recommendation(service, compliance):
    # This logic mimics the Vertex AI grounding in the KSG Productivity Strategy
    if compliance >= 100:
        return "Target met. Maintain current service standards."
    
    knowledge_base = {
        "Training Certificates": "Variance due to manual verification. Action: Implement Digital Signature Workflows as per Strategy Sec 4.1.",
        "Consultancy Enquiries": "Delayed response. Action: Decentralize enquiry handling to Departmental Liaisons.",
        "Revenue Mobilization": "Shortfall detected. Action: Execute the AWP SO_6 Resource Mobilization Strategy immediately."
    }
    return knowledge_base.get(service, "Review internal process bottlenecks and realign with FY 2025/26 targets.")

def generate_ksg_report(achievements):
    report_data = []
    for item in achievements:
        # Calculate % Compliance: (Target / Actual) * 100
        compliance = (item['target'] / item['actual']) * 100 if item['actual'] > item['target'] else 100
        compliance = round(compliance, 1)
        
        report_data.append({
            "Service": item['service'],
            "Target": f"Within {item['target']} Days",
            "Actual": f"{item['actual']} Days",
            "Compliance": f"{compliance}%",
            "AI_Corrective_Action": get_ksg_ai_recommendation(item['service'], compliance)
        })
    return report_data

# DEMO DATA: Simulating a month at the CCSE
demo_input = [
    {"service": "Training Certificates", "target": 5, "actual": 8},
    {"service": "Consultancy Enquiries", "target": 2, "actual": 1}
]

print(json.dumps(generate_ksg_report(demo_input), indent=4))
