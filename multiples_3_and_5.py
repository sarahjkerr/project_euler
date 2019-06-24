t = []

for i in range(1,1000):

    if i%3 == 0:
        t.append(i)
    elif i%5 == 0:
        t.append(i)
    else:
        pass
    
print(sum(t))
