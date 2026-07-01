class Solution:
    @staticmethod
    def HalfDiamond(n):
        for i in range (1,2*n-1):
           for j in range(1,i+1):
               print("*", end=" ") 
           print("")
           for k in range(1,n-i+1):
               print("*", end=" ")
           print("")

obi = Solution
n = 5
print(obi.HalfDiamond(n))