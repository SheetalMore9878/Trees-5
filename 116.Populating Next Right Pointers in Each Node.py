# """
# Approach2: Most optimal, Worked , connections and BST
# """
# #Time and space O(n)

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return None

        level=root
        while(level.left!=None):
            curr=level #first node of every level
            while (curr!=None):
                curr.left.next=curr.right
                if(curr.next!=None): #if not last node of level
                    curr.right.next=curr.next.left

                curr=curr.next

            level=level.left

        return root

