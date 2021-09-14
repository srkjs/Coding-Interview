# O(n) Time | O(n) Space
def sortedSquaredArray(array):
    res = [0 for i in array]
    start = 0
    end = len(array) - 1
    idx = len(res) - 1
    while idx >= 0:
        startVal = array[start]
        endVal = array[end]
        if abs(startVal) > abs(endVal):
            res[idx] = startVal**2
            start += 1
        else:
            res[idx] = endVal**2
            end -= 1
        idx -= 1
    return res  


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

