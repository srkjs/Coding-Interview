# O(n) Time | O(1) Space
def longestPeak(array):
    ans = 0
    i = 1
    while i < len(array) - 1:
        
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i+=1
            continue
        
        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1
        
        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right+=1
            
        currPeak = right - left - 1
        ans = max(currPeak, ans)
        i = right

    return ans



import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)

if __name__ == '__main__':
    unittest.main()