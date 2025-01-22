class Solution(object):
    def inPalindrome(self,x):
        num = str(x)
        
        return num == num[::-1]
    
x = 121
sol = Solution()

print(sol.inPalindrome(x))