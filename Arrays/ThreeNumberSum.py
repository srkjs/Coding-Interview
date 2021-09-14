# O(n^2) Time | O(n) Space
def threeNumberSum(array, targetSum):
    answers=[]
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currSum = array[i] + array[left] + array[right]
            if currSum == targetSum:
                answers.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currSum < targetSum:
                left += 1
            elif currSum > targetSum:
                right -= 1
    return answers
			
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])


if __name__ == '__main__':
    unittest.main()