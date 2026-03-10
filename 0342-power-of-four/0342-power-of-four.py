class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(x):
            if x == 1:
                return True
            if x <= 0 or x % 4 != 0:
                return False
            return power(x // 4)
        
        
        return(power(n))