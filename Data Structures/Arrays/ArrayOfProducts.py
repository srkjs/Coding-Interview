# O(n) Time | O(n) Space
def arrayOfProducts(array):
    output = [1 for _ in array]
    leftProduct = 1
    for i in range(len(array)):
        output[i] = leftProduct
        leftProduct *= array[i]

    rightProduct = 1
    for i in reversed(range(0, len(array))):
        output[i] *= rightProduct
        rightProduct *= array[i]

    return output

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        actual = arrayOfProducts(array)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()