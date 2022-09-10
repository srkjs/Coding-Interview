# Leetcode question 155 - https://leetcode.com/problems/min-stack/

# minMaxStack keeps track of minValue and maxValue at a particular instance.
"""
For example,
	- push 2 to stack
		stack - [2]
		minMaxStack - [[2, 2]]
	- push 3 to stack
		stack - [2, 3]
		minMaxStack - [[2, 2], [2, 3]]
	- push 1 to stack
		stack - [2, 3, 1]
		minMaxStack - [[2, 2], [2, 3], [1, 3]]
"""

# So whenever we pop an element from stack, the min & max value is not lost
"""
For example,
	stack - [2, 3, 1]
	minMaxStack - [[2, 2], [2, 3], [1, 3]]
	- pop() from stack
		stack - [2, 3]
		minMaxStack - [[2, 2], [2, 3]] # In this case the minVal 1 is popped and 2 becomes new minVal.
	- pop() from stack
		stack - [2]
		minMaxStack - [[2, 2]] # In this case the maxVal 3 is popped and 2 becomes new maxVal.
"""

# Time - O(1) for each function | Space - O(n + n), where n is number of elements pushed.
class MinStack(object):
	
    def __init__(self):
        self.stack = []
        self.minMaxStack = []
		
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.minMaxStack) == 0:
            self.minMaxStack.append([val, val])
        elif self.minMaxStack[-1][0] > val:
            self.minMaxStack.append([val, self.minMaxStack[-1][1]])
        elif self.minMaxStack[-1][0] < val:
            self.minMaxStack.append([self.minMaxStack[-1][0], val])
        else:
            self.minMaxStack.append(self.minMaxStack[-1])
        
    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack):
            self.stack.pop()
            self.minMaxStack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minMaxStack):
            return self.minMaxStack[-1][0]