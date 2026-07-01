'''
*****
*****
*****
*****
*****
'''
class Solution:
    def Rectangular_Star(n):
     for i in range (0,n):
        for j in range (0,n):
            print("*" , end=" ")
        print()


print(Solution.Rectangular_Star(5))