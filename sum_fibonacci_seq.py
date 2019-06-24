def fib_calc(i):
    a, b = 0, 1
    while a < i:
        if not a % 2:         
            yield a
        a, b = b, a + b 
        
 print(sum(fib_calc(4000000)))
