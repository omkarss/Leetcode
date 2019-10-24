



def rotate(nums, k ):

    
    for i in range(0,int(len(nums)/2)):

        #nums = swap(nums,i,(len(nums)%((len(nums)%k)+i)))
        pos_swap =(k%len(nums)+i)%len(nums)
        c = nums[i]
        nums[i] = nums[pos_swap]
        nums[pos_swap] = c
        print(nums)


rotate([1,2,3,4,5,6,7],3)

