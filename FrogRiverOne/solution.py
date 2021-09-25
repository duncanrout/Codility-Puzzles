def solution(X, A):
    #My plan is to create a new array of 1-X and delete elements
    #in that array that pop up while iterating thru the original array. 

    #Time complexity is O(n^2) I believe, for this attempt I will keep
    #time complexity to this value.

    tempArray = []
    for r in range(X):
        tempArray.append(r+1)

    count = 0
    for i in A:
        
        if i in tempArray:
            tempArray.remove(i)
    
        #if array is empty
        if not tempArray:
            return count
        count = count + 1
    
    return -1
