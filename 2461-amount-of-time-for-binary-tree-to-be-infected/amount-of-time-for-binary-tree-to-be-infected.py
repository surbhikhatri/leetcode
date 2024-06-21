# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # apply bfs? need to get cur node's children and parent
        adj = defaultdict(list)
        if not root.left and not root.right:
            return 0

        def getadj(root):
            if root:
                if root.left:
                    adj[root.val].append(root.left.val)
                    adj[root.left.val].append(root.val)
                   

                if root.right:
                    adj[root.val].append(root.right.val)
                    adj[root.right.val].append(root.val)
            
                getadj(root.left)
                getadj(root.right)

        getadj(root)
        q = [start]
        res = [-1]
        visited = set()
        tmp = []

        while q:
            while q:
                tmp.append(q.pop()) # level wise 
            if tmp:
                for node in tmp:
                    if node not in visited:
                        for val in adj[node]:
                            if val not in visited:
                                q.append(val) # for next level
                        
                        visited.add(node)
                res[0] += 1
            tmp = []

        return res[0]


        

        q, res, infected, tmp = [start], [-1], set(), []
        
        while q:
            while q:
                tmp.append(q.pop())
            if tmp:
                for inf in tmp:
                    if inf not in infected:
                        for val in adj_list[inf]:
                            if val not in infected:
                                q.append(val)

                        infected.add(inf)
                res[0] += 1
            tmp = []

          
        return res[0]




        