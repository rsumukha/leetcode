"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

#YOU CAN REPRESENT GRAPH IN A DICTIONARY
# BFS and DFS doesnt matter if you use stack/queue since the order doesnt matter, we process all its neighbors and add to s/q and process
# immediatly or later, 

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = collections.deque()
        queue.append(node)
        visited = {}
        newnode_ = Node(node.val, [])
        visited[node] = newnode_      #the visited dictionary will have reference to the nodes
        
        while queue:
            cur = queue.popleft()       # 1->2->3 pop the current
            for child in cur.neighbors:  #for all its neighbours
                if visited.get(child, None)!=None:      #if child node is alreday created add link
                    visited[cur].neighbors.append(visited[child])
                else:                                   #else create child node
                    newnode = Node(child.val, [])
                    visited[child] = newnode
                    visited[cur].neighbors.append(newnode)
                    queue.append(child)
  
        return newnode_
                    
    def dfs(self, node):
        for child in node.neighbors:
            if self.visited.get(child, 0):
                self.visited[node].neighbors.append(self.visited[child])
            else:
                newnode = Node(child.val, [])
                self.visited[child] = newnode
                self.visited[node].neighbors.append(newnode)
                self.dfs(child)
                

            
            
        
