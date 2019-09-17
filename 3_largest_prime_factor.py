"""There are a few options for this one, ranging in levels of elegance"""

"""Option 1: Let's brute force this and then eyeball the results - This won't hold up performance-wise, so
   it should be avoided for bigger calculations.
   
   Background: This problem is asking about factors, so we know the number is a composite. This means its prime factors
   are less than or equal to its square root, which decreases the range we have to iterate over. When we output a list of factors,
   we check to see if they're divisible by each other, and grab the largest only divisible by itself*****."""
   
def find_factors(x):
    
    factors = []
    
    sqrt = int(x**(0.5))
    
    for y in range(1,sqrt):
        if (x % y) == 0:
            factors.append(y)
            
    return factors
    
def check_list(g):
    
    copied = g.copy()
    
    for item in g:
        for otheritem in copied:
            if item % otheritem == 0:
                print(str(item) + " can be divided by " + str(otheritem))

my_list = find_factors(600851475143)
#[1, 71, 839, 1471, 6857, 59569, 104441, 486847]

check_list(my_list)
#1 can be divided by 1
#71 can be divided by 1
#71 can be divided by 71
#...
#486847 can be divided by 71
#486847 can be divided by 6857*****
#486847 can be divided by 486847
