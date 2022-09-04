class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) Time | O(n^2) Space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertInTrie(i,string)

    def insertInTrie(self,i,string):
        node=self.root
        for j in range(i,len(string)):
            letter=string[j]
            if letter not in node:
                node[letter]={}
            node=node[letter]
        node[self.endSymbol]=True
    
    # O(m) Time | O(1) Space
    def contains(self, string):
        node=self.root
        for letter in string:
            if letter not in node:
                return False
            node=node[letter]
        return True if self.endSymbol in node else False


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trie = SuffixTrie("babc")
        expected = {
            "c": {"*": True},
            "b": {"c": {"*": True}, "a": {"b": {"c": {"*": True}}}},
            "a": {"b": {"c": {"*": True}}},
        }
        self.assertEqual(trie.root, expected)
        self.assertTrue(trie.contains("abc"))


if __name__ == '__main__':
    unittest.main()