def findMaxIndex(arr):
    maxIndex = 0
    maxValue = arr[0]
    for i in range(len(arr)):
        if arr[i] >= maxIndex:
            maxIndex = i
            maxValue = arr[i]
    return maxIndex

print(findMaxIndex([1,2,1,3,5,6,4]))
    