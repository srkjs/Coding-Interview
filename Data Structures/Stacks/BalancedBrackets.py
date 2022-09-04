# O(n) Time | O(n) Space 
def balancedBrackets(brackets):
    openingBrackets = "{[("
    closingBrackets = "}])"
    dic = {"}":"{", ")":"(", "]":"["}

    stack = []

    for bracket in brackets:
        if bracket in openingBrackets:
            stack.append(bracket)
        elif bracket in closingBrackets:
            if not len(stack):
                return False
            if stack[-1] == dic[bracket]:
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)


if __name__ == '__main__':
    unittest.main()