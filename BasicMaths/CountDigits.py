class Solution:
    def countdigits(n):
        num = n
        count = 0

        while num !=0:
            num = num //10
            count +=1
        print(count)

    
obj = Solution
print(obj.countdigits(89075))

# num = 12345
# count = 0

# while num != 0:
#     num //= 10
#     count += 1

# print(count) 