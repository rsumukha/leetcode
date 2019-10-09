"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

#YOU CAN REPRESENT GRAPH IN A DICTIONARY


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
                    


            
            
        
