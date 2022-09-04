# O(n) Time | O(n) Space
def spiralTraverse(matrix):
    answer = []
    sR, eR = 0, len(matrix) - 1
    sC, eC = 0, len(matrix[0]) - 1

    while sR <= eR and sC <= eC:
        
        for c in range(sC, eC + 1):
            answer.append(matrix[sR][c])
            
        for r in range(sR+1, eR+1):
            answer.append(matrix[r][eC])
        
        for c in reversed(range(sC, eC)):
            if sR == eR:
                break
            answer.append(matrix[eR][c])
        
        for r in reversed(range(sR+1, eR)):
            if sC == eC:
                break
            answer.append(matrix[r][sC])	
        
        sR+=1
        eR-=1
        sC+=1
        eC-=1

    return answer

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(spiralTraverse(matrix), expected)



if __name__ == '__main__':
    unittest.main()