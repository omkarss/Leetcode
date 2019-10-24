


def calcmax(height):
    start = 0 
    end = len(height)-1
    max_area= 0

    while(start<end):

        

        if(max_area<min(height[start],height[end])*(end - start)):
            max_area = min(height[start],height[end])*(end - start)
        
        if(height[start]>height[end]):
            end = end - 1
        else:
            start = start + 1
    
    return max_area


print(calcmax([1,2,9]))