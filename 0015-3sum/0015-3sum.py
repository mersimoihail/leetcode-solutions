class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        li = []
        nums.sort()
        for i in range(n-2):
            left = i+1
            right = n-1
            if i >0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                su = nums[i] +nums[left] + nums[right]

                if su == 0:
                    
                
                    li.append([nums[left],nums[right],nums[i]])
                    while left < right and nums[left] ==nums[left+1]   :
                        
                        left +=1
                    while left < right and nums[right] == nums[right-1]  :
                        
                        right -=1
                    left +=1
                    right -=1

                elif su >0:
                    right -=1
                else:
                    left += 1
        return li
