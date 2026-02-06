class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        swap = 0
        ones = 0
        while i < len(s):
            if s[i] == '1':
                ones +=1
            else:
                swap += ones
            i += 1
        return swap

        
        