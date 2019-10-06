class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,
             "IV":4,
             "V":5,
             "IX":9,
             "X":10,
             "XL":40,
             "L":50,
             "XL":90,
            "C" :100,
             "CD":400,
             "D":500,
             "CM":900,
             "M":1000
            }
        
        total=0
        prev=-1
        for s in s[::-1]:
            cur=d.get(s)
            if cur>=prev:
                total+=cur
            else:
                total-=cur
            prev=cur
                
        return total
