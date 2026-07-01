class Solution:
    @staticmethod
    def Right_aligned_triangle(n):
        for i in range(n+1):
            for i in range(1,i+1):
                print("*", end=" ")
            print()
obj = Solution
n = 5
print(obj.Right_aligned_triangle(n))