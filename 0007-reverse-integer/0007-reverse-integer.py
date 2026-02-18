import math
class Solution:
    def reverse(self, x: int) -> int:
        
        x_str=str(x)
        s=[]
        for i in range(len(x_str)):
            s.append(x_str[i])
        
        rev=""
        for i in range(len(s)):
            rev=rev+s.pop()
        
        if(rev[-1] =="-"):
            rev = "-"+rev[:-1]
            

        rev_int = int(rev)

        if -2**31 <= rev_int <= 2**31 - 1:
            return rev_int
        else:
            return 0        