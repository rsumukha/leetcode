class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if maxWidth <= 0:
            return [None]
        if len(words) == 0:
            return []
        
        output = []
        currentline, width = [], 0
        
        
        def resize(currentline, width, maxwidth):
            # print(currentline, width, maxwidth)
            if len(currentline)==1:                         # if there is only one word in the line append spaces
                return currentline[0]+" "* (maxwidth -width) #at the end
            else:
                numberofspaces = maxwidth - width
                locations = len(currentline)-1
                spacesarray = locations * [numberofspaces // locations] #assign equal spaces to all the locations
                remainingspaces = numberofspaces % locations
                for i in range(remainingspaces):
                    spacesarray[i]+=1
                out=""
                for i in range(locations):
                    out += currentline[i]+" "*spacesarray[i]
                out+=currentline[i+1]
                return out
                
        
        for word in words:
            if width + len(word) + len(currentline) > maxWidth:
                output.append(resize(currentline, width, maxWidth))
                currentline, width = [word], len(word)
            else:
                currentline.append(word)
                width += len(word)
        output.append(" ".join(currentline)+ " "* (maxWidth - width - len(currentline)+1))
        return output
        
        

