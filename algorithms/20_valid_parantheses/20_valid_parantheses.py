"""
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


def isValid(s):
    """Check if sequence of parantheses are valid

    :param s: TODO
    :returns: TODO

    """
    stack = []
    matching = {"}": "{", "]": "[", ")": "("}
    for item in s:
        if item in matching.values():
            stack.append(item)
        else:
            # item in matching.values():
            close = stack.pop() if stack else "!"
            if matching[item] != close:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid(")]"))
