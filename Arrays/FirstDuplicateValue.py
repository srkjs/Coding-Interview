# O(n) Time | O(1) Space
def firstDuplicateValue(array):
    for num in array:
        absValue = abs(num)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = firstDuplicateValue(input)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()