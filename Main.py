import math
import matplotlib.pyplot as plt
from random import *
ty = 2.58
def pi_error(x_):
    return ty*math.sqrt(math.pi/4*(1-math.pi/4)/x_)
out = open("output.txt", "w")
for i in range(10):
    n = 10**6
    k = 0
    for i in range(n):
        x = random()
        y = random()
        if (x**2 + y**2<= 1):
            k+=1
    w = k/n
    delta = ty*math.sqrt(w*(1-w)/n)
    #print("k = " + str(k) + " n = " + str(n), file = out)
    print(str(w*4) + " +- " + str(delta*4) + "; probability = 0.99", file = out)
    print("Difference = " + str(abs(w*4-math.pi)), file = out)
    #print("Disp: " + str(n*math.pi/4*(1-math.pi/4)), file = out)
    print("End.\n", file = out)
out.close()
xs = [2**k for k in range(10,25)]
ys = [pi_error(x) for x in xs]
plt.plot(xs, ys)
plt.xscale('log')
plt.xlabel('Number of points')
plt.ylabel('Error')
plt.title('Decrease of error relative to number of points')
plt.show()