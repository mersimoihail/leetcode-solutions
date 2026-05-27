class Solution:
    def fib(self, n: int) -> int:
        
        def fi(n,n_1,n_2):
            for i in range(n):
                temp = n_1
                n_1 = n_1+n_2
                n_2 = temp
            return n_2
        if n == 1 or n ==0:
            return n
        else:
            
            return fi(n,1,0)




               
            
            
        