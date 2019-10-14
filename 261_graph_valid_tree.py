class Solution(object):
    def validTree(self, n, edges):
        #if i dfs then there shouldnt be cycle and to be a vaild tree dont traverse back to its parent
        # handle parent prune dfs if it is a parent
        if n==1:
            return True
        if len(edges) == 1 and n==2:
            return True
    
            
        graph = {}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [0 for _ in range(n)]
        count = []
        def dfs(i, parent):
            count.append(i)
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            visited[i] = -1
            for node in graph[i]:
                if node!= parent and not dfs(node, i):
                    return False
            visited[i] = 1
            return True
        
        
        if not dfs(0, 0):
            return False
        if len(count)==n:
            return True
        return False
        
