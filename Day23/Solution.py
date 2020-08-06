import sys
from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            print("New node")
            return Node(data)
        else:
            if data<=root.data:
                print("left")
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                print("right")
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    # def enqueueNodes(self, s):
    #   self.queue.append(s)

    def levelOrder(self, root):
    # Write your code here
        nodes = list()
        nodes.append(root)
        nodes_searched = ''
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            nodes_searched += str(node.data) + ' '
        print(nodes_searched)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
print(root)
myTree.levelOrder(root)