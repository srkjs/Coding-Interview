# Average - O(n^2) Time | O(n^2) Space
# Worst - O(n^3) Time | O(n^2) Space

def fourNumberSum(array, targetSum):
    hashTable = {}
    answers = []
    for i in range (1, len(array) - 1):
        for j in range (i + 1, len(array)):
            currSum = array[i] + array[j]
            difference = targetSum - currSum
            if difference in hashTable:
                for pairs in hashTable[difference]:
                    answers.append(pairs + [array[i], array[j]])
        
        for k in range(0, i):
            currSum = array[i] + array[k]
            if currSum in hashTable:
                hashTable[currSum].append([array[k], array[i]])
            else:
                hashTable[currSum] = [[array[k], array[i]]]
                
    return answers

import unittest


def sortAndStringify(array):
    return ",".join(sorted(list(map(lambda x: str(x), array))))


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
        output = list(map(sortAndStringify, output))
        quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]
        self.assertTrue(len(output) == 2)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)


if __name__ == '__main__':
    unittest.main()