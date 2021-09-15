class MinMaxStack:
    def __init__(self):
        self.minMaxStack=[]
        self.stack=[]
    
    # O(1) Time | O(1) Space
    def peek(self):
        return self.stack[-1]

    # O(1) Time | O(1) Space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) Time | O(1) Space
    def push(self, number):
        newMinMax={"min":number, "max":number}
        if len(self.minMaxStack):
            lastMinMax=self.minMaxStack[-1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
    
    # O(1) Time | O(1) Space
    def getMin(self):
        return self.minMaxStack[-1]["min"]

    # O(1) Time | O(1) Space
    def getMax(self):
        return self.minMaxStack[-1]["max"]

import unittest


def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)

if __name__ == '__main__':
    unittest.main()