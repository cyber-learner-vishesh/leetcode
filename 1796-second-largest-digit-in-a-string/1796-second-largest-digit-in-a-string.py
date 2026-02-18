class Solution:
    def secondHighest(self, s: str) -> int:
        s_et=set()
        for i in range(len(s)):
            if s[i].isdigit() == True :
                s_et.add(s[i])
        sorted_list = sorted(s_et)
        if len(sorted_list)>1:
            return int(sorted_list[-2])
        else:
            return -1
        
        