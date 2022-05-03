# Leetcode question 973 - https://leetcode.com/problems/k-closest-points-to-origin/
def findRestaurants(allLocations, numberOfRequiredRestaurants):

    distanceSortedArray = []
    for location in allLocations:
        distance = (((location[0]) ** 2) + ((location[1]) ** 2)) ** 0.5
        distanceSortedArray.append([distance, location])
    distanceSortedArray.sort(key = lambda x : x[0])
    print(distanceSortedArray)
    result = []
    for i in range(numberOfRequiredRestaurants):
        result.append(distanceSortedArray[i][1])
    return result

# All test-cases passed
def findRestaurants2(allLocations, numberOfRequiredRestaurants):
    if numberOfRequiredRestaurants == 0:
        return []
    hashTable = {}
    array, result = [], []
    for location in allLocations:
        distance = (((location[0]) ** 2) + ((location[1]) ** 2)) ** 0.5
        if distance not in hashTable:
            hashTable[distance] = [location]
            array.append(distance)
        else:
            hashTable[distance].append(location)
    
    array.sort()
    for distance in array:
        locations = hashTable[distance]
        for location in locations:
            if numberOfRequiredRestaurants > 0:
                result.append(location)
                numberOfRequiredRestaurants -= 1
        if numberOfRequiredRestaurants == 0:
            return result


testCaseOne = [[[1, 2], [3, 4], [1, -1]], 1]
testCaseTwo = [[[1, 3], [2, -2]], 1]
testCaseThree = [[3,3],[5,-1],[-2,4], 2]


print(findRestaurants(testCaseOne[0], testCaseOne[1]))
print(findRestaurants(testCaseTwo[0], testCaseTwo[1]))
print(findRestaurants(testCaseThree[0], testCaseThree[1]))

print(findRestaurants2(testCaseOne[0], testCaseOne[1]))
print(findRestaurants2(testCaseTwo[0], testCaseTwo[1]))
print(findRestaurants2(testCaseThree[0], testCaseThree[1]))