class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma = nums[0]
        su = nums[0]
        for i in range(1,len(nums)):
            if su > 0:
                su +=nums[i]
                if su < 0:
                    su = nums[i]
                        
            else:
                su = nums[i]
            ma = max(su,ma)
        return ma

            


            
        