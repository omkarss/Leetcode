
def threeSumClosest(nums, target):
    
    closest_sum = 99999
    sum_found = False
    sum_elements = 0 
    for i in range(0,len(nums)):
        
        if(sum_found == True):
            return sum_elements
        
        j = len(nums)-1
        k = i + 1


        while(j>k):
            temp = arr[i] + arr[j] +arr[k]
            
            if(temp < target):
                k = k  + 1

            elif(temp > target):
                j = j - 1

            if(abs(target - temp) < closest_sum):
                closest_sum = abs(target - temp)
                sum_elements = temp
            
            if(temp == target):
                return temp


        
    return sum_elements
        
    


        




arr =[-1,0,1,1,55]
arr.sort()
target =   3
print(threeSumClosest(arr,target))
