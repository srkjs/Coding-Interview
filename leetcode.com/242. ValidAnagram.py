# Leetcode question 242 - https://leetcode.com/problems/valid-anagram/

# Solution 1
# Time - O(n) | Space - O(n), where n is max(len(s), len(t))
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hT = dict()
    for char in s:
        if char not in hT:
            hT[char] = 0
        hT[char] += 1
    
    for char in t:
        if char not in hT or hT[char] == 0:
            return False
        hT[char] -= 1
    
    for key in hT:
        if hT[key] != 0:
            return False

    return True


# Solution 2
# Time - O(n * log(n)), where n is max(len(s), len(t)) | Space - O(1)
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    str1 = sorted(s)
    str2 = sorted(t)
    
    return True if str1 == str2 else False
