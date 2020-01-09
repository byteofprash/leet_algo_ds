"""
 Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
    """Longest palindrome of the given string

    :param s: TODO
    :returns: TODO

    """
    res = ""
    for i, _ in enumerate(s):
        substr = ""
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            substr = s[left+1:right]
        res = substr if len(substr) > len(res) else res
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            substr = s[left+1:right]
        res = substr if len(substr) > len(res) else res

    return res

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("xabax"))
