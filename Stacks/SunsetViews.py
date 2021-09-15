# O(n) Time | O(n) Space
def sunsetViews(buildings, direction):
    if not len(buildings):
        return []
    ans = []
    if direction == "EAST":
        ans.append(len(buildings)-1)
        val = buildings[-1]
        for i in reversed(range(len(buildings) - 1)):
            currVal = buildings[i]
            if currVal > val:
                ans.append(i)
                val = currVal
        ans.reverse()
    else:
        ans.append(0)
        val = buildings[0]
        for i in range(1, len(buildings)):
            currVal = buildings[i]
            if currVal > val:
                ans.append(i)
                val = currVal
    return ans

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"
        expected = [1, 3, 6, 7]
        actual = sunsetViews(buildings, direction)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()