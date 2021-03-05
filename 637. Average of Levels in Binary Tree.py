# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
initialize an average_array,
do a level order traversal ,
at each level append the average of the values
"""
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # base check
        if not root : return None
        queue = deque()
        next = deque()
        queue.append(root)
        average = []
        traversal = []
        while queue:
            cur = queue.popleft()
            traversal.append(cur.val)
            if cur.left:
                next.append(cur.left)
            if cur.right:
                next.append(cur.right)
            if len(queue) == 0:
                queue,next = next,queue
                average.append(self.average_level(traversal))
                traversal = []
        return average

    def average_level(self,traversal):
        return sum(traversal)/len(traversal)


# Time complexity : O(n)
# space complexity :O(n)


                

                
        


        