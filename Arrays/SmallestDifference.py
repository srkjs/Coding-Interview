# O(nlog(n) + mlog(m)) Time | O(1) Space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0 
    currDiff = float("inf")
    smallestDiff = float("inf")
    answer = []
    while i < len(arrayOne) and j < len(arrayTwo):
        num1 = arrayOne[i]
        num2 = arrayTwo[j]
        if num1 < num2:
            currDiff = num2 - num1
            i += 1
        elif num1 > num2:
            currDiff = num1 - num2
            j += 1
        else:
            return [num1, num2]
        
        if currDiff < smallestDiff:
            smallestDiff = currDiff
            answer = [num1,num2]
        
    return answer



import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])



if __name__ == '__main__':
    unittest.main()