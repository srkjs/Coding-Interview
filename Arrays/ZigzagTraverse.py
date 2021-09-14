# O(n) Time | O(n) Space
def zigzagTraverse(array):
    lastRow=len(array)-1
    lastCol=len(array[0])-1
    ans=[]
    row,col=0,0
    goingDown=True
    while row>=0 and col>=0 and row<len(array) and col<len(array[0]):
        ans.append(array[row][col])
        if goingDown:
            if col == 0 or row == lastRow:
                goingDown = False
                if row == lastRow:
                    col+=1
                else:
                    row+=1
            else:
                row+=1
                col-=1
        else:
            if row==0 or col==lastCol:
                goingDown=True
                if col==lastCol:
                    row+=1
                else:
                    col+=1
            else:
                row-=1
                col+=1
    return ans

# def isOutOfBound(row,col,height,width):
# 	return row<0  or row>height or col<0 or col>width

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        self.assertEqual(zigzagTraverse(test), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])



if __name__ == '__main__':
    unittest.main()