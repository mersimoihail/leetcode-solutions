class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def next_index(current):
            """Calculate next index with proper wrap-around"""
            return (current + nums[current]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
                
            slow, fast = i, i
            direction = nums[i] > 0
            
            while True:
                # Check and move slow
                next_slow = next_index(slow)
                if (nums[next_slow] > 0) != direction:
                    break
                slow = next_slow
                
                # Check and move fast (first step)
                next_fast = next_index(fast)
                if (nums[next_fast] > 0) != direction:
                    break
                fast = next_fast
                
                # Check and move fast (second step)
                next_fast = next_index(fast)
                if (nums[next_fast] > 0) != direction:
                    break
                fast = next_fast
                
                # Check for cycle
                if slow == fast:
                    # Ensure it's not a single element cycle
                    if slow != next_index(slow):
                        return True
                    break
            
            # Mark all visited nodes in this path to avoid re-checking
            # This optimization reduces time complexity
            current = i
            current = i
            while nums[current] != 0 and (nums[current] > 0) == direction:
                next_curr = next_index(current)
                nums[current] = 0
                current = next_curr

        
        return False