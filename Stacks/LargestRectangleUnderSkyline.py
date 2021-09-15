def largestRectangleUnderSkyline(buildings):
    area = 0
    for i in range(len(buildings)):
        j = k = i
        currArea = 0
        while j > 0 and buildings[j - 1] >= buildings[i]:
            j -= 1
        while k < len(buildings) - 1 and buildings[k + 1] >= buildings[i]:
            k += 1
        currArea += buildings[i] * (k - j + 1)
        area = max(area, currArea)
    return area

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 3, 3, 2, 4, 1, 5, 3, 2]
        expected = 9
        actual = largestRectangleUnderSkyline(input)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()