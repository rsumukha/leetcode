# check if a graph has a cycle
# convert the graph to adjacency lists,(undirected and directed graph)
# have visiting and visited set or array (it has index so it isnt that costly, for some it is better to use #array(scorecalculation)). add nodes to visited if it is already done so that we dont have to dfs it again
# visiting is the current visiting set  (visited in other problems)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == None:
            return False
        if numCourses == 1:
            return True
        visiting = set()
        visited = set()
        graph = {}
        for i in range(numCourses):
            graph[i] = []        
        for x,y in prerequisites:
            graph[x].append(y)
            
        def dfs(i):
            if i in visited:
                return True
            if i in visiting:
                return False
            
            visiting.add(i)
            for item in graph[i]:
                if not dfs(item):
                    return False
            visiting.remove(i)
            visited.add(i)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
