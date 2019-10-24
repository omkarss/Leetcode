def find132pattern(nums):
    N = len(nums)
    arr = list(nums)
    for i in range(1,N):
        arr[i] = min(nums[i-1], arr[i-1])
        
    j = N
    for i in range(N)[::-1]:
        if nums[i] <= arr[i]: 
            continue
        while j < N and arr[j] <= arr[i]:
            j += 1
        if j < N and arr[j] < nums[i]:
            return True
        if nums[i] > arr[i - 1]:
            j -= 1
            arr[j] = nums[i]
      
    return False

print(find132pattern([1,3,2]))