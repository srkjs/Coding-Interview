def nonConstructibleChange(coins):
    coins.sort()
    minChange = 1
    for num in coins:
        if num > minChange:
            return minChange
        minChange += num
    return minChange