class Solution:
    def countGoodNumbers(self, n: int) -> int:
        ev = 0
        od = 0
        MOD = pow(10,9) + 7
        if n%2 !=0:
            ev = (n//2)+1
        else:
            ev += (n//2)
        od = n//2
        print(ev,od)
        return pow(5,ev,MOD)*pow(4,od,MOD)%MOD
        
            