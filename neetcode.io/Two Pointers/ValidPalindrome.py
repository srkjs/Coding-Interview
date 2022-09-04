# Leetcode question 125 - https://leetcode.com/problems/valid-palindrome/

# Solution 1
# Time - O(n), where n is len(s) | Space - O(1)
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and s[i].isalnum() is False:
            i += 1
        while j > i and s[j].isalnum() is False:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

# Solution 2
# Time - O(n) | Space - O(n), where n is len(s)
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    chars = []
    for char in s:
        if char.isalnum() is True:
            chars.append(char.lower())
    i = 0
    j = len(chars) - 1
    while i < j:
        if chars[i] != chars[j]:
            return False
        i += 1
        j -= 1
    return True
