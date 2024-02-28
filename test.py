# Liste af betting sites med opdaterede værdier
import json
import sys
sites = sys.stdin.read()
sites = json.loads(sites)

# Funktion til at generere alle mulige kombinationer og finde den mest balancerede med det højeste samlede afkast
def find_best_combination(sites):
    from itertools import product

    # Genererer alle mulige kombinationer (1, X, 2) for hver betting site
    outcomes = list(product(["1", "X", "2"], repeat=len(sites)))
    
    max_return = 0
    best_combination = None
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
            max_return = min_return
            best_combination = outcome

    return best_combination, max_return

# Find den bedste kombination
best_combination, max_return = find_best_combination(sites)
best_combination, max_return

print(json.dumps({"best_combination": best_combination, "max_return": max_return}))

