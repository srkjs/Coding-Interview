# O(n) Time | O(n) Space
def largestRange(array):
    hashTable = {}
    answer = []
    longestLength = 0
    for num in array:
        hashTable[num] = True

    for num in array:
        if hashTable[num] is False:
            continue
        hashTable[num] = False
        currLength = 1
        left = num - 1
        right = num + 1
        while left in hashTable:
            hashTable[left] = False
            currLength += 1
            left -= 1
        while right in hashTable:
            hashTable[right] = False
            currLength += 1
            right += 1
        if currLength > longestLength:
            longestLength = currLength
            answer = [left + 1, right - 1]
            
    return answer

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])


if __name__ == '__main__':
    unittest.main()