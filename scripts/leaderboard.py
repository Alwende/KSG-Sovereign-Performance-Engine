import json

# Institutional Performance Data
campuses = [
    {"name": "Lower Kabete (CCSE)", "score": 98.2},
    {"name": "Baringo Campus", "score": 94.5},
    {"name": "Embu Campus", "score": 88.1},
    {"name": "Mombasa Campus", "score": 82.3}
]

def rank_institutions(data):
    # Sort by score descending
    ranked = sorted(data, key=lambda x: x['score'], reverse=True)
    print("\n=== KSG INSTITUTIONAL RANKING (MARCH 2026) ===")
    for i, campus in enumerate(ranked, 1):
        status = "TOP PERFORMER" if i == 1 else "REMEDIAL REQUIRED" if campus['score'] < 85 else "STABLE"
        print(f"Rank {i}: {campus['name']} - {campus['score']}% [{status}]")

rank_institutions(campuses)
