# O(n) Time | O(1) Space
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            isNonDecreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()