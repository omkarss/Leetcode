#class Solution:
import re
import math

def calculate(s):
     
    if(len(s)<1):
        return 0

    if (('+' not in s) and ('-' not in s) and ('*' not in  s) and ('/' not in s)):
        return(int(s))
            


    s=s.replace(' ','')

    str_total = ''
    lst=[]
    i = 0
    while(i < len(s)):
        str_total = ''
        if(s[i] not in ['/','*','+','-']):
            while(s[i] not in ['/','*','+','-']):
                str_total += s[i]
                i = i + 1
                if(i >= len(s)):
                    break

            lst.append(str_total)
        else:
            lst.append(s[i])
            i = i + 1

    
    total = 0
    i = 0
    stack = []
    while(i<len(lst)):
        if((lst[i] == '*') or (lst[i]== '/')) :
            stack.append(lst[i])
            stack.append(lst[i+1])
            x,op,y = stack.pop(),stack.pop(),stack.pop()
            if(op == '/'):
                total = math.floor(int(y)/int(x))
                stack.append(total)    
            else:
                total = int(x)*int(y)
                stack.append(total)

            i = i + 2 

        else:
            stack.append(lst[i])
            i = i + 1
    
    
    if(len(stack)<=1):
        return total 
    total = 0
    
    if(stack[1] == '+'):
        total = int(stack[0]) + int(stack[2])
    else:
        total = int(stack[0]) - int(stack[2])
    i = 3
    while(i<len(stack)):
        if(stack[i] == '+'):
            x = stack[i+1]
            total = total  + int(x)
            i = i + 2
        elif(stack[i] == '-'):
            x = stack[i+1]
            total = total - int(x)
            i = i + 2
        else:
            i = i + 1

    return total


    


#s =Solution()
print(calculate("340+876-65/45/98+876-90-876*21"))

        