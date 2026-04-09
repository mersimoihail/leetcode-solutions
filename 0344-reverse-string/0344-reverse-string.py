class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(left , right):
            if right < left:
                return
            s[right] , s[left] = s[left] , s[right]
            reverse(left+1 , right-1)
            
        rgt = len(s)-1
        reverse(0,rgt)