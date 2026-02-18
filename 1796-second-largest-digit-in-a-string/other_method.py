class Solution:
    def secondHighest(self, s: str) -> int:
        first=float('-inf')
        second=float('-inf')
        for i in range(len(s)):
            if (s[i].isdigit()):
                if (int(s[i])>first):
                    second = first
                    first=int(s[i])
                else:
                    if(int(s[i])>second and int(s[i])!=first):
                        second = int(s[i])
            
        if(second==float("-inf")):
            return -1
        else:
            return second
            
        
        
