class Solution:
    @staticmethod
    def RightAngledNumberPyramid(n):
        for i in range(n):
            for j in range(1,n-i+1):
                print("*", end=" ")
            print()
obj = Solution
n = 5
print(obj.RightAngledNumberPyramid(n))