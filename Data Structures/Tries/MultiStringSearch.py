# O(ns + bs) Time | O(ns) Space
def multiStringSearch(bigString, smallStrings):
    trie=Trie()
    for string in smallStrings:
        trie.insert(string)
    containedStrings={}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString,i,trie,containedStrings)
    return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string,startIdx,trie,containedStrings):
    currNode=trie.root
    for i in range(startIdx,len(string)):
        currChar=string[i]
        if currChar not in currNode:
            break
        currNode=currNode[currChar]
        if trie.endSymbol in currNode:
            containedStrings[currNode[trie.endSymbol]]=True
            
class Trie:
    def __init__(self):
        self.root={}
        self.endSymbol="*"
        
    def insert(self,string):
        curr=self.root
        for i in range(len(string)):
            if string[i] not in curr:
                curr[string[i]]={}
            curr=curr[string[i]]
        curr[self.endSymbol]=string


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]),
            [True, False, True, True, False, True, False],
        )




if __name__ == '__main__':
    unittest.main()