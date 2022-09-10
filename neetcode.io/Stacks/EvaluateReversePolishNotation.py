# Leetcode question 150 - https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Time - O(n) | Space - O(n), where n is len(tokens)
def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    operators = "+-*/"
    
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            
            if token == "+":
                res = num1 + num2 
            elif token == "-":
                res = num1 - num2 
            elif token == "*":
                res = num1 * num2 
            elif token == "/":
                res = float(num1) / float(num2)
                
            stack.append(int(res))
            
    return stack[-1]