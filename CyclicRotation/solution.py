def solution(A, K):
    try:
        #Given an array, rotate elements by 1.
        #I plan to take the last element, and stick it to the front. Then delete the last element.
        def rotate(A):
            lastEle = A[-1]
            newArray = A
            newArray.insert(0, lastEle)
            newArray.pop(-1)
            A = newArray

        #Rotate the array K times
        for x in range(K):
            rotate(A)
        return A

    #In the case that the array is empty...    
    except:
        return A
