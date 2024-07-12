import json
import sys
from itertools import product

# Læs betting sites data fra standard input
customers = sys.stdin.read()
customers = json.loads(customers)

"""
Eksempeldata:
customers = [
    [
        {"site": "unibet", "homeWin": 4000, "draw": 6000, "awayWin": 8000, "money": 2000},
        ...
    ],
    ...
]
"""

def find_best_combination(sites, previous_outcomes):
    max_return = 0
    best_combination = None

    # Generer alle mulige kombinationer af udfald (1, X, 2) for hver betting site
    outcomes = list(product(["1", "X", "2"], repeat=len(sites)))
    
    for outcome in outcomes:
        total_returns = [0, 0, 0]  # Indekser: 0 -> hjemmevind, 1 -> uafgjort, 2 -> udeholdvind
        for i, result in enumerate(outcome):
            if result == "1":
                total_returns[0] += sites[i]["homeWin"]
            elif result == "X":
                total_returns[1] += sites[i]["draw"]
            elif result == "2":
                total_returns[2] += sites[i]["awayWin"]
        
        min_return = min(total_returns)
        if min_return > max_return:
            # Tjek forskellighed fra tidligere outcomes
            differences = [sum(1 for a, b in zip(outcome, prev) if a != b) for prev in previous_outcomes]
            min_difference = min(differences) if differences else float('inf')
            
            if min_difference > 0:  # Vi tillader ikke præcise gentagelser
                max_return = min_return
                best_combination = {
                    "combination": [site["site"] for site in sites],
                    "outcome": outcome,
                    "difference": min_difference
                }

    return best_combination, max_return

# Behandl hver kundes data individuelt
results = []
previous_outcomes = []

for customer_sites in customers:
    best_combination, max_return = find_best_combination(customer_sites, previous_outcomes)
    if best_combination:
        previous_outcomes.append(best_combination["outcome"])
    results.append({
        "best_combination": best_combination,
        "min_return": max_return
    })

# Udskriv resultatet som JSON
print(json.dumps(results))
