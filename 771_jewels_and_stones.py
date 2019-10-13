class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        myset = set(J)
        _sum_ = 0
        for ele in S:
            if ele in myset:
                _sum_ += 1
        return _sum_
