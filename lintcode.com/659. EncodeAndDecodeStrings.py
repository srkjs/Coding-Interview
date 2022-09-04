# Lintcode question 659 - https://www.lintcode.com/problem/659/description

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
# Time - O(n) | Space - O(n), where n is len(strs)
def encode(self, strs):
    encodedStr = "".join("#897#" + word for word in strs)
    return encodedStr


"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
# Time - O(n), where n is len(strs) | Space - O(1)
def decode(self, str):
    return str.split("#897#")[1:]