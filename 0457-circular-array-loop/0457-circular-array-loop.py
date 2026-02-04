class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next_ele(current):
            return (current + nums[current])%n
        for i in range(n):
            if nums[i] == 0:
                continue
            fast,slow = i,i
            direction = nums[i] >0
            while True:
                next_sl = next_ele(slow)
                if (nums[next_sl] >0 )!= direction:
                    break
                slow = next_sl
                next_fast = next_ele(fast)
                if (nums[next_fast] >0) != direction:
                    break
                fast = next_fast
                next_fast = next_ele(fast)
                if (nums[next_fast] >0) != direction:
                    break
                fast = next_fast
                if fast == slow:
                    if slow != next_ele(slow):
                        return True
                    break
        return False
