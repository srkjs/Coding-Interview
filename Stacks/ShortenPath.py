# O(n) Time | O(n) Space
def shortenPath(path):
    startsWithSlash = True if path[0] == "/" else False
    tokens = []
    paths = path.split("/")
    for token in paths:
        if isImpToken(token):
            tokens.append(token)
    stack=[] 
    if startsWithSlash:
        stack.append("")
        
    for token in tokens:
        if token=="..":
            if len(stack) == 0 or stack[-1] == "..":
                stack.append("..")
            elif stack[-1] != "":
                stack.pop()	
        else:
            stack.append(token)
            
    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)

def isImpToken(token):
    return len(token)>0 and token != "."


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = "/foo/bar/baz"
        output = shortenPath("/foo/../test/../test/../foo//bar/./baz")
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()