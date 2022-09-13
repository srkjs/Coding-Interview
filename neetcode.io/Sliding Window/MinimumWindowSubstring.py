# Leetcode question 76 - https://leetcode.com/problems/minimum-window-substring/

# Time - O(n) | Space - O(n), where n is len(string)
def minWindow(self, string, substring):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    substringCount = {}
    for char in substring:
        substringCount[char] = 1 + substringCount.get(char, 0)

    window = {}
    
    need = len(substringCount)
    have = 0
    
    res = [-1, -1]
    
    l = 0
    for r in range(len(string)):
        currChar = string[r]
        window[currChar] = 1 + window.get(currChar, 0)
        if currChar in substringCount and window[currChar] == substringCount[currChar]:
            have += 1
        
        while have == need:
            # update our result
            if res[1] - res[0] > r - l or res[0] == -1:
                res = [l, r]

            # pop from left of our window
            leftChar = string[l]
            window[leftChar] -= 1
            if leftChar in substringCount and window[leftChar] < substringCount[leftChar]:
                have -= 1
            l += 1
    
    l, r = res
    return string[l : r + 1] if l != float("inf") else ""