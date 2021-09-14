# O(n) Time | O(n) Space
def minRewards(scores):
    ans = [1 for ele in scores]

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            ans[i] = ans[i - 1] + 1
            
    for i in reversed(range(len(scores)-1)):
        if scores[i] > scores[i + 1]:
            ans[i] = max(ans[i], ans[i + 1] + 1)

    return sum(ans)


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)


if __name__ == '__main__':
    unittest.main()