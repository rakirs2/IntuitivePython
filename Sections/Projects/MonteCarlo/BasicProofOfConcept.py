import random

points = []
hits = 0
total = 100000
for i in range(total):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    points.append((x,y))
    if x *x + y*y < 1:
        hits+=1

print (hits/total * 4)
