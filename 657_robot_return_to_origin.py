class Solution(object):
    def judgeCircle(self, moves):
        if len(moves) == 0:
            return None
        if len(moves)==1:
            return False
        
        start = [0,0]
        for move in moves:
            if move=="U":
                start[0], start[1] = start[0]-1, start[1]
            elif move=="D":
                start[0], start[1] = start[0]+1, start[1]
            elif move=="R":
                start[0], start[1] = start[0], start[1]+1
            elif move=="L":
                start[0], start[1] = start[0], start[1]-1
        if start[0]==0 and start[1]==0:
            return True
        else:
            return False
                
        
