# O(n) Time | O(1) Space
def isValidSubsequence(array, sequence):
    arrIdx=0
    seqIdx=0
    while arrIdx<len(array) and seqIdx<len(sequence):
        if array[arrIdx]==sequence[seqIdx]:
            seqIdx+=1
        arrIdx+=1
    return True if seqIdx==len(sequence) else False