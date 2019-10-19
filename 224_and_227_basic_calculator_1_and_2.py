class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return None
        if len(s) == 1:
            return int(s)
        
        valuestack = []
        operatorstack = []
        i=0
        while i<len(s):
            token = s[i]            
            if token == " ":
                i+=1
                continue                
            elif token.isdigit():
                token=""
                while i<len(s) and s[i].isdigit():
                    token += s[i]
                    i+=1
                valuestack.append(token)
                i -= 1            
            elif token == ")":                
                while len(operatorstack)!=0 and operatorstack[-1] != "(":
                    op2 = valuestack.pop()
                    op1 = valuestack.pop()
                    op = operatorstack.pop()
                    valuestack.append(str(self.applyoperation(op1, op2, op)))
                operatorstack.pop()                
            elif token == "(":
                operatorstack.append(token)                
            elif token == "+" or token == "-" or token =="*" or token == "/":
                while len(operatorstack)!=0 and self.checkprecedence(operatorstack[-1])>=self.checkprecedence(token):
                    op2 = valuestack.pop()
                    op1 = valuestack.pop()
                    op = operatorstack.pop()
                    valuestack.append(str(self.applyoperation(op1, op2, op)))
                operatorstack.append(token)
            i+=1
        
        while len(operatorstack)!=0:
            op2 = valuestack.pop()
            op1 = valuestack.pop()
            op = operatorstack.pop()
            valuestack.append(str(self.applyoperation(op1, op2, op)))
        
        return valuestack[-1]
                
    
    def applyoperation(self, op1, op2, op):
        if op == "+": return int(op1)+int(op2)
        if op == "-": return int(op1)-int(op2)
        if op == "*": return int(op1)*int(op2)
        if op == "/": return int(int(op1)/int(op2))
        
    def checkprecedence(self, op):
        if op == "+" or op == "-":
            return 1
        if op == "*" or op == "/":
            return 2
        return 0
        
        
