"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(x):
    """Is palindrome or not

    :param x: TODO
    :returns: TODO

    """
    word = str(x)
    l, r = 0, len(word) -1
    while l < r:
        if word[l] != word[r]:
            return False
        l+=1
        r-=1

    return True

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(1001))
