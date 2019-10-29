class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        graph = {}        
        #build graph
        for i, item in enumerate(stones):
            graph[item] = i
        cache = set()
        visited = set()
        
        def dfs(node, jump):
            if node in visited:
                return False
            if (node,jump) in cache:
                return False
            if node == stones[-1]:
                return True
            visited.add(node)
            for eachjump in [jump, jump+1, jump-1]:
                if node+eachjump in graph and (not node+eachjump in visited):
                    if dfs(node+eachjump, eachjump):
                        return True   
            visited.remove(node)
            cache.add((node, jump))
            return False
        
        return dfs(0,0)
        
