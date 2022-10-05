# Leetcode question 74 - https://leetcode.com/problems/search-a-2d-matrix/

# Time - O(nlogn + mlogm), where n is len(matrix[0] & m is len(matrix)) | Space - O(1)
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = 0
    n = len(matrix[0]) - 1
    
    while m >= 0 and n >= 0 and m < len(matrix) and n < len(matrix[0]):
        currVal = matrix[m][n]

        if currVal < target:
            m += 1
        elif currVal > target:
            n -= 1
        else:
            return True
        
    return False