#Can reduce full list to check, since if a number is divisible by 18, it's also divisible by 6 and 3, and so on and so on
#Can also start at 2520 and increment up by 20

nums = [11, 13, 14, 16, 17, 18, 19, 20]

for x in range(2520, 9999999999, 20):
    if all(x % y == 0 for y in nums):
        print(x)
        
#232792560
