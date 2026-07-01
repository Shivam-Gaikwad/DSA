# """# *****
# # *****
# # *****
# # *****
# #""" *****


def square(n):
    for i in range (0,n):
        for j in range (0,n):
            print('*', end=" ")
        print()
print(square(4))

def triangle(n):
    for i in range (0,n):
        for j in range (0,i+1):
            print('*', end=" ")
        print()
print(triangle(4))

def reverse_triangle(n):
    for i in range (n,0,-1):
        for j in range (i):
            print('*', end=" ")
        print()
print(reverse_triangle(4))

def num_triangle(n):
    for i in range (0,n):
        for j in range (0,i+1):
            print(j, end=" ")
        print()
print(num_triangle(4))

def reverse_num_triangle(n):
    for i in range (n,0,-1):
        for j in range (i , 0 ,-1):
            print(j, end=" ")
        print()
print(reverse_num_triangle(4))