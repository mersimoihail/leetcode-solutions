class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lis = []
        ans = 1 
        lis.append(ans)
        for i in range(rowIndex+1):
            ans *= (rowIndex - i)
            ans /= i+1
            holder = int (ans)
            lis.append(holder)
        lis.pop()
        return lis

        