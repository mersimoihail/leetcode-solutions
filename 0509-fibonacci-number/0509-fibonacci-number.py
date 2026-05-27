class Solution:
    def fib(self, n: int) -> int:
        
        def fi(n):
            if n == 0 or n ==1:
                return n
            
            else:
                return fi(n-1) + fi(n-2)

             
        return fi(n)



               
            
            
        