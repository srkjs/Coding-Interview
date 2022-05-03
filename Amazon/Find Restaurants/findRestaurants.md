# Find X nearby Vegetarian Restaurants


>##  [Leetcode Question 973 - K Closest points to origin](https://leetcode.com/problems/k-closest-points-to-origin/ "leetcode.com")
<br />

Amazon's Alexa team is working on optimizing the customer experience for scenarios where customers ask generic questions. One example of a generic question is "What are good vegetarian restaurants nearby?" In this example, Alexa would then search for a list of vegetarian restaurants in the city and select the nearest X vegetarian restaurants relative to the customer's location. 
<br />
<br />
Given an array representing the locations of N vegetarian restaurants in the city, implement an algorithm to find the nearest X vegetarian restaurants to the customer's location.
<br />
<br />
**Note:** The customer begins at the location (0, 0). The distance from the customer's current location to a recommended vegetarian restaurant location (x, y) is the square root of x2 + y².
<br />
<br />
> **Example**
<br />
Input : *allLocations* = [[1, 2], [3, 4], [1, -1]], *numRestaurants* = 2
<br />
<br />
Output : [[1, -1], [1, 2]]
<br />
The distance of the customer's current location from location [1, 2] is square root(5) = 2.236.
<br />
The distance of the customer's current location from location [3, 4] is square root(25) = 5. 
<br />
The distance of the customer's current location from location [1,-1] is square root(2)= 1.414.
<br />
The required number of nearest vegetarian restaurants to the customer's location is 2, hence the output is [1,-1] and [1, 2].
<br />

## **Solution -**
```Python
def findRestaurants(allLocations, numberOfRequiredRestaurants):
    distanceSortedArray = []
    for location in allLocations:
        distance = (((location[0]) ** 2) + ((location[1]) ** 2)) ** 0.5
        distanceSortedArray.append([distance, location])
    
    distanceSortedArray.sort(key = lambda x : x[0])
    result = []
    for i in range(numberOfRequiredRestaurants):
        result.append(distanceSortedArray[i][1])
    return result
```
## **Complexity -**
> Time : O(n * log(n)), where n is the number of locations in the given `allLocations` array.

> Space : O(n), where n is the number of locations in the given `allLocations` array.

<br />
Refer - 

[Solution](findRestaurants.py "Password Strength").
