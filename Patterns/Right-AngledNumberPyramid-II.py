class Solution:
    @staticmethod
    def RightAngledNumberPyramid2(n):
        for i in range(n+1):
            for j in range(1,i+1):
                print(i, end=" ")
            print()
obj = Solution
n = 5
print(obj.RightAngledNumberPyramid2(n))