"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

def letterCombinations(digits):
    """TODO: Docstring for letterCombinations.

    :param digits: TODO
    :returns: TODO

    """
    if digits == "":
        return []
    vals = {2:["a",'b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']}
    from itertools import product
    lists = [vals[int(x)] for x in digits]
    ret = product(*lists)
    ret_vals = []
    for item in ret:
        ret_vals.append("".join(item))
    return ret_vals

print(letterCombinations("232"))
print(letterCombinations(""))
