class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        ret = [0 for i in range(len(cells))]
        N= N % 14
        if N == 0:
            N=14
        while N:
            for i in range(1, len(cells)-1):
                ret[i] = 1 if not(cells[i-1] ^ cells[i+1]) else 0
            cells = ret[:]
            N-=1
            # print(ret, 15-N)

        return ret
