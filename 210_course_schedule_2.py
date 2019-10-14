class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if numCourses == 1:
            return [0]
        if len(prerequisites)==None:
            return None
        
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
        answer = []
        visited, visiting = set(), set()
        
        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True
            visiting.add(i)
            for node in graph[i]:
                if not dfs(node):
                    return False

            visiting.remove(i)
            visited.add(i)
            answer.append(i)
            return True
        
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []
        return answer
