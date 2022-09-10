# Leetcode question 22 - https://leetcode.com/problems/generate-parentheses/

# Time - O() | Space - O() - Complex to analyze
def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    # Only add open parenthesis if openBracketsCount < n
    # Only add close parenthesis if closingBracketsCount < openBracketsCount
    # Valid IFF openBracketsCount == closingBracketsCount == n
    
    res = []
    
    def backtrack(openBracketsCount, closingBracketsCount, parenthesis):
        # 2 * n = openBracketsCount + closingBracketsCount
        # Eg: n = 3 -> 2 * 3 = 6 = len("((()))")
        # So, if 3 == "(((" == ")))" - add to result
        if n == openBracketsCount == closingBracketsCount:
            res.append(parenthesis)
            return
        
        if openBracketsCount < n:
            backtrack(openBracketsCount + 1, closingBracketsCount, parenthesis + "(")
            
        if closingBracketsCount < openBracketsCount:
            backtrack(openBracketsCount, closingBracketsCount + 1, parenthesis + ")")
        return
    
    # Start with single open bracket
    backtrack(1, 0, "(")
    return res