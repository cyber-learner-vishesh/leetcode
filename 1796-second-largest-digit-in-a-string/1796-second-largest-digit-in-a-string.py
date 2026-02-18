class Solution:
    def secondHighest(self, s: str) -> int:
        first=0
        second=-1
        for i in range(len(s)):
            if (s[i].isdigit()):
                if (int(s[i])>first):
                    temp = first
                    second=temp
                    first = int(s[i])
                else:
                    if(int(s[i])>second):
                        second = int(s[i])
            
        if(second==first):
            return -1
        else:
            return second
            
        
        