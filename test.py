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

# Funktion til at generere alle mulige kombinationer og finde den mest balancerede med det højeste samlede afkast
def find_best_combination(sites, previous_outcome=None):
    max_return = 0
    best_combination = None

    # Generer alle mulige kombinationer af udfald (1, X, 2) for hver betting site
    outcomes = list(product(["1", "X", "2"], repeat=len(sites)))
    
    for outcome in outcomes:
        if outcome == previous_outcome:
            continue  # Skip hvis det er samme som tidligere kundes resultat

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
            max_return = min_return
            best_combination = {
                "combination": [site["site"] for site in sites],
                "outcome": outcome
            }

    return best_combination, max_return

# Behandl hver kundes data individuelt
results = []
previous_outcome = None
for customer_sites in customers:
    best_combination, max_return = find_best_combination(customer_sites, previous_outcome)
    previous_outcome = best_combination['outcome'] if best_combination else None
    results.append({
        "best_combination": best_combination,
        "min_return": max_return
    })

# Udskriv resultatet som JSON
print(json.dumps(results))