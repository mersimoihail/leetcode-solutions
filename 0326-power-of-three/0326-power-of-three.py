class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def power(x):
            if x == 1:
                return True
            if x <= 0 or x %3 != 0:
                return False
            else:
                return power(x//3)
        return power(n)
        