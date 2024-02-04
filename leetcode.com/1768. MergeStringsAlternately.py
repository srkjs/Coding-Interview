def mergeAlternately(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    mergedString = []
    i, j = 0, 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            mergedString.append(word1[i])
            i += 1
        if j < len(word2):
            mergedString.append(word2[j])
            j += 1
    return "".join(mergedString)
