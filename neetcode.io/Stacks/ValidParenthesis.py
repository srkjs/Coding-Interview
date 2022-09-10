# Leetcode question 20 - https://leetcode.com/problems/valid-parentheses/

# Time - O(n) | Space - O(n), where n is len(s)
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    openingBrackets = "([{"
    closingBrackets = ")]}"
    stack = []
    matchingBracket = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    for bracket in s:
        if bracket in openingBrackets:
            stack.append(bracket)
        elif bracket in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] != matchingBracket[bracket]:
                return False
            else:
                stack.pop()
    return True if not len(stack) else False