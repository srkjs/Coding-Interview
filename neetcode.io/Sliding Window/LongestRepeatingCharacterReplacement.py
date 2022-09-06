# Leetcode question 424 - https://leetcode.com/problems/longest-repeating-character-replacement/

# Time - O(26 * n), where n is len(s) | Space - O(26)
def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    count = {}
    left = 0
    res = 0
    
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        # windowSize = right + 1 - left
        if (right + 1 - left - max(count.values())) > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, right + 1 - left)
        
    return res

# Time optimized Solution
# Time - O(n), where n is len(s) | Space - O(26)
def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    count = {}
    left = 0
    res = 0
    maxFrequency = 0
    
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxFrequency = max(maxFrequency, count[s[right]])
        # windowSize = right + 1 - left
        if right + 1 - left - maxFrequency > k:
            count[s[left]] -= 1
            left += 1
            
        res = max(res, right + 1 - left)
    
    return res