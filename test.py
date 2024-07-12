import json
import sys
from itertools import product, combinations

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
def find_best_combination(sites):
    max_return = 0
    best_combination = None

    # Generer kombinationer for 1, 2 og 3 kunder
    for num_customers in range(1, 4):
        customer_combinations = list(combinations(sites, num_customers))
        
        for customer_comb in customer_combinations:
            outcomes = list(product(["1", "X", "2"], repeat=len(customer_comb)))
            
            for outcome in outcomes:
                total_returns = [0, 0, 0]  # Indekser: 0 -> hjemmevind, 1 -> uafgjort, 2 -> udeholdvind
                
                for i, result in enumerate(outcome):
                    if result == "1":
                        total_returns[0] += customer_comb[i]["homeWin"]
                    elif result == "X":
                        total_returns[1] += customer_comb[i]["draw"]
                    elif result == "2":
                        total_returns[2] += customer_comb[i]["awayWin"]
                
                min_return = min(total_returns)
                if min_return > max_return:
                    max_return = min_return
                    best_combination = {
                        "combination": [site["site"] for site in customer_comb],
                        "outcome": outcome
                    }

    return best_combination, max_return

# Behandl hver kundes data individuelt
results = []
for customer_sites in customers:
    best_combination, max_return = find_best_combination(customer_sites)
    results.append({
        "best_combination": best_combination,
        "min_return": max_return
    })

# Udskriv resultatet som JSON
print(json.dumps(results))
