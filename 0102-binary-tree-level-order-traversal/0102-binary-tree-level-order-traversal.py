# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        tot = []
        while queue:
            lis = []
            leng = len(queue)
            for _ in range (leng):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                lis.append(cur.val)
            tot.append(lis)
        return tot

        
        




        