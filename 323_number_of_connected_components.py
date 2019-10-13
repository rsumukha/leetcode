class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n ==0:
            return 0
        if n==1:
            return 1
        
        graph ={}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])  #check if the graph is undirected or directed
            graph[edge[1]].append(edge[0])
        
        visited = set()
        numofcomponents = 0
        
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for node in graph[i]:
                dfs(node)
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                numofcomponents +=1
        return numofcomponents
