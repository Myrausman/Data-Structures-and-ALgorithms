from lliststack import Stack

def isValidSource(srcfile):
    s = Stack()
    position = Stack()
    err = list()
    openbrackets=["{","[","("]
    closebrackets = ["}","]",")"]
    linenum=0
    colnum=0
    for line in srcfile:
        linenum+=1
        colnum=0
        for token in line:
            colnum+=1
            if token in openbrackets:
                s.push(token)
                p = errorPosition(linenum,colnum)
                position.push(p)
            elif token in closebrackets:
                if s.isEmpty():
                    #return False
                    return "line "+str(linenum)+", column "+str(colnum)
                else:
                    left = s.pop()
                    pos = position.pop()
                    if (token == "}" and left != "{") or \
                            (token == "]" and left != "[") or \
                            (token == ")" and left != "("):
                        # return False
                        return "line " + str((pos.line)) + ", column " + str(pos.column)


    #return s.isEmpty()
    if s.isEmpty():
        return str("No issues in brackets delimiters of code")
    else:
        while not position.isEmpty():
            p=position.pop()
            print('Error: '+s.pop()+', linenumber: '+str(p.line)+', column:'+str(p.column))
        return True

class errorPosition:
    def __init__(self, line=0, column=0):
        self.line=line
        self.column=column
    def __repr__(self):
        return f"{self.line} and {self.column}"

file = open('sourcecode.c','r')
result = isValidSource(file)
print(result)