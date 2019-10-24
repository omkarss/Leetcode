class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        nums.sort()
        
        
        op= []
        
        if(len(nums)<3):
            return([])
        
        elif(all(v == 0 for v in nums)):
            return([[0,0,0]])
            
        
        for i in range(0,len(nums)):
        
        
            l = i + 1
            r = len(nums) - 1
            
        
            while(l<r):
            

                if(nums[i] + nums[l] + nums[r] < 0):
                    l = l + 1
            
                elif(nums[i] + nums[l] + nums[r] > 0):
                    r = r - 1

                else:
                    op.append([nums[i],nums[l],nums[r]])
                    l = l + 1
                    r = r - 1

        return(list(set(map(tuple,op))))
            




            
            
            
        