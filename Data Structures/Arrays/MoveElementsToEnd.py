# O(n) Time | O(1) Space
def moveElementToEnd(nums, toMove):
    def swap(i, j, a):
            a[i], a[j] = a[j], a[i]
            
    idxToBeUpdated = 0
    for i in range(len(nums)):
        if nums[i] != toMove:
            swap(idxToBeUpdated, i, nums)
            idxToBeUpdated += 1
    return nums

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        expectedStart = [1, 3, 4]
        expectedEnd = [2, 2, 2, 2, 2]
        output = moveElementToEnd(array, toMove)
        outputStart = sorted(output[0:3])
        outputEnd = output[3:]
        self.assertEqual(outputStart, expectedStart)
        self.assertEqual(outputEnd, expectedEnd)

if __name__ == '__main__':
    unittest.main()
