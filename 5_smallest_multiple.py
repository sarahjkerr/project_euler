#Can reduce full list to check, since if a number is divisible by 18, it's also divisible by 6 and 3, and so on and so on

nums = [11, 13, 14, 16, 17, 18, 19, 20]
answer_list = []

for x in range(2520, 99999999, 20):
    if all(x % y == 0 for y in nums):
        answer_list.append(x)
        
min(answer_list)
