class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def ch(no):
            if no == 4:
                return True
            if no < 4 :
                return False
            return ch(no/4)
        if n == 1:
            return True
        return ch(n)