# Leetcode question 567 - https://leetcode.com/problems/permutation-in-string/

# Efficient Solution
# Time - O(n), where n is len(s2) | Space - O(26)
def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    
    if len(s1) > len(s2):
        return False
    
    s1Count = [0] * 26
    s2Count = [0] * 26
    
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
    
    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0
    
    left = 0
    for right in range(len(s1), len(s2)):
        
        if matches == 26:
            return True
        
        idx = ord(s2[right]) - ord("a")
        s2Count[idx] += 1
        if s2Count[idx] == s1Count[idx]:
            matches += 1
        elif s1Count[idx] == s2Count[idx] - 1:
            matches -= 1
        
        idx = ord(s2[left]) - ord('a')
        s2Count[idx] -= 1
        if s1Count[idx] == s2Count[idx]:
            matches += 1
        elif s1Count[idx] == s2Count[idx] + 1:
            matches -= 1
        left += 1
        
    return matches == 26

# Passes all test cases, but in-efficient solution
# Time - O((n - m) * n) | Space - O(26), where n is len(s2) & m is len(s1)
def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    s1Dict = {}
    for char in s1:
        s1Dict[char] = 1 + s1Dict.get(char, 0)
    
    for i in range(len(s2) - len(s1) + 1):
        s2Dict = {}
        for j in range(i, i + len(s1)):
            char = s2[j]
            s2Dict[char] = 1 + s2Dict.get(char, 0)
        
        for key in s1Dict:
            if key not in s2Dict:
                break
            s2Dict[key] -= s1Dict[key]
        
        validPermutation = True
        for key in s2Dict:
            if s2Dict[key] != 0:
                validPermutation = False
        
        if validPermutation:
            return True
        
    return False