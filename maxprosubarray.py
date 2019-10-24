def maxsubarray(arr):

    if(len(arr) == 1):
        return(arr[0])

    maxarray = [-9999]*len(arr)
    maxarray_dummy = [-9999]*len(arr)

    
    maxarray[0] = arr[0]
    maxarray_dummy[0] = arr[0]
    
    for i in range(1,len(arr)):
c        maxarray[i] = max(arr[i],arr[i]*maxarray[i-1])

    maxarray_dummy.sort()
    maxarray.sort()
    return(max(maxarray[-1],maxarray_dummy[-1]))
        




print(maxsubarray([-2,3,-4]))