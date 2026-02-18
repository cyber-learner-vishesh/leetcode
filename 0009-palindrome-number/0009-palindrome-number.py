class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str=str(x)
        length = len(x_str)
        
        
        palandrom = True
        for i in range(int(length/2)):
            if(x_str[i]!=x_str[length-1-i]):
             return False

        return True        

