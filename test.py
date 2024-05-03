import json
import sys
from itertools import product

def find_best_combination(sites):
    # Genererer alle mulige kombinationer (1, X, 2) for hver betting site
    outcomes = list(product(["1", "X", "2"], repeat=len(sites)))
    
    max_return = 0
    best_combination = None
    best_returns = None
    
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
            best_returns = total_returns

    return best_combination, max_return, best_returns

# Modtag data fra stdin eller en anden kilde
sites_input = json.loads(sys.stdin.read()) 

# Find den bedste kombination
best_combination, max_return, best_returns = find_best_combination(sites_input)

# Print resultatet
print(json.dumps({
    "best_combination": best_combination, 
    "min_return": max_return,
    "returns_per_outcome": best_returns
}))
