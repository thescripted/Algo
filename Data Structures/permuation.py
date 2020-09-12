# Example of string permutation in Python.

def permutation(string):
    memo = {}
    return _permute("", string, memo)

def _permute(preset, subset, memo):
    initialpreset = preset
    initialsubset = subset
    if subset == "":
        return [preset]
    
    if subset in memo:
        return []
    sol = []
    for index, char in enumerate(subset):
        preset = initialpreset + char
        if index == 0:
            subset =  initialsubset[index+1:]
        elif index == len(subset):
            subset = initialsubset[:index]
        else:
            subset = initialsubset[:index] + initialsubset[index + 1:]
        sol.append(_permute(preset, subset, memo))
    
    memo[initialsubset] = sol
    return sol

print(permutation("abcd"))