# O(n) Time | O(n) Space
def nextGreaterElement(array):
    res = [-1 for num in array]
    stack = []
    
    for i in range(2 * len(array)):
        i = i % len(array)
        while len(stack) and array[stack[-1]] < array[i]:
            top = stack.pop()
            res[top] = array[i]
        stack.append(i)
        
    return res

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 5, -3, -4, 6, 7, 2]
        expected = [5, 6, 6, 6, 7, -1, 5]
        actual = nextGreaterElement(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()