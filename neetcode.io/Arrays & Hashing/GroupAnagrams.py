# Leetcode question 49 - https://leetcode.com/problems/group-anagrams/

# Time - O(n * m * log(m)) | Space - O(n), where n is len(strs) & m is length of largest word in strs
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dic = {}
    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord not in dic:
            dic[sortedWord] = [word]
        else:
            dic[sortedWord].append(word)
    return list(dic.values())
    