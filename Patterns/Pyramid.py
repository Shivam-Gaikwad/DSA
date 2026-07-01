class Solution:
    @staticmethod
    def pyramid(n):
        for i in range(n):
            for j in range(0,n-i-1):
                print(" " , end=" ")
            for k in range(0, i*2+1):
                print("*", end=" ")
            for j in range(0,n-i-1):
                print(" " , end=" ")
            print()
obj = Solution
n = 5
print(obj.pyramid(n))