

def sumpofsubarray(W,n,arr):
    if(W==0):
        return True
    
    elif(W<0 or n < 0):
        return False
    
    else:
        return(sumpofsubarray(W,n-1,arr) or sumpofsubarray(W-arr[n],n-1,arr))
    


print(sumpofsubarray(81,len([1, 2, 3, 4, 5, 7, 8, 12, 20, 35, 61, 80])-1,[1, 2, 3, 4, 5, 7, 8, 12, 20, 35, 61, 80]))




    