# Leetcode question 239 - https://leetcode.com/problems/sliding-window-maximum/

# Time - O(n * k) | Space - O(k), where n is len(nums) & k is window size. 
def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # Deque or Double Ended Queue is a type of queue in which insertion and removal of elements can either be performed from the front or the rear.
    
    deque = [] # [ [idx, elementAtIdx], ... ]
    
    # NOTE : This deque should be implemented in such a way, where 
    #      - it holds only the elements which are inside the current window (i.e) from idx i to i + (k - 1). (k - 1 is because idx i starts from 0). So len(deque) is always <= windowSize (k).
    #      - it holds the largest value of currentWindow at the first position of deque.
    
    res = []
    
    for i, ele in enumerate(nums):
        # print("Current index i - ", i)
        
        # startIdx for currentWindow = i - k, where i is current index and k is size of window
        # while condition:
        #       - when deque != null and
        #       - idx of 1st element in deque is less than startIdx of current window
        # keep popping deque from front, since deque should only hold the elements which are from the current Window
        while deque and deque[0][0] <= i - k:
            popped = deque.pop(0)
            # print("Popping from front since the index of max element so far is now less than startIdx of currentWindow(i - k) - ", popped)
        
        # while condition:
        #       - when deque != null and
        #       - idx of last element in deque is less than value of current element
        # keep popping deque from rear, since deque should hold the element with maxVal at front (or) there is no need for deque to store elements which are lesser than the currentValue because from now on, currentValue will be the maxValue
        while deque and deque[-1][1] <= ele:
            popped = deque.pop()
            # print("Popping from rear since the value of current Ele is greater than the value of element present in the last Index of deque - ", popped)
            
        deque.append([i, ele])
        # print("Deque append ", deque)
        
        # This if statement is added since we populate result only after traversing first 'k' elements
        if i + 1 >= k:
            res.append(deque[0][1])
            # print("res ", res)
            
    return res