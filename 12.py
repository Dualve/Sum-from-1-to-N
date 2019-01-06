from math import fabs
a = int(input())
total = 0
if a > 0:
    total = int(((1+a)*a)/2)
elif a == 0:
    total = 1
else:
    total = int(((1+a)*(fabs(a)+2))/2)
    
print(total)
