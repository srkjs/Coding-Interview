# Leetcode question 36 - https://leetcode.com/problems/valid-sudoku/

# Time - O(9 * 9) | Space - O(9)
def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rowDict = dict()
    colDict = dict()
    threeCrossThreeDict = dict()
    for r in range(len(board)):
        for c in range(len(board[0])):
            fieldValue = board[r][c]
            if fieldValue == ".":
                continue
            if (r in rowDict and fieldValue in rowDict[r]) or (c in colDict and fieldValue in colDict[c]) or (str(r//3) + str(c//3) in threeCrossThreeDict and fieldValue in threeCrossThreeDict[str(r//3) + str(c//3)]):
                return False
            rowDict[r] = (fieldValue,) if r not in rowDict else rowDict[r] + (fieldValue,)
            colDict[c] = (fieldValue,) if c not in colDict else colDict[c] + (fieldValue,)
            threeCrossThreeDict[str(r//3) + str(c//3)] = (fieldValue,) if str(r//3) + str(c//3) not in threeCrossThreeDict else threeCrossThreeDict[str(r//3) + str(c//3)] + (fieldValue,)
    return True