# O(n) Time | O(1) Space
def subarraySort(array):
    minNum = float("inf")
    maxNum = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
    if minNum == float("inf") and maxNum == float("-inf"):
        return [-1,-1]
    leftPos = 0
    while minNum >= array[leftPos]:
        leftPos += 1
    rightPos = len(array)-1
    while maxNum <= array[rightPos]:
        rightPos -= 1
    return [leftPos, rightPos]

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), [3, 9])



if __name__ == '__main__':
    unittest.main()