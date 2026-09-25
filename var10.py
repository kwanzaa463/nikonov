from math import *
for x in range(10,150,5):
    a = 10
    b = 150
    y = (x/100)**(1/2*(x/100))+((x/100)**2*log(x/100**3)/sin(x/100)**2+cos(x/100)**2)
    print(y)
