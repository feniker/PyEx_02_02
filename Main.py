import math
import matplotlib.pyplot as plt
import numpy as np
ty = 2.58
def pi_error(x_):
    return math.sqrt(math.pi/4*(1-math.pi/4)/x_)
out = open("output.txt", "w")
n = 10**6
k = 0
xs = [2**k for k in range(10,25)]
ys = [pi_error(x) for x in xs]
N = {2**k for k in range(10,25)}
arr = np.random.rand(2**24+1, 2) - 0.5
mask = np.sum(arr**2, axis=-1) < 0.25
arr_pi = [np.count_nonzero(mask[:i])/i*4 for i in xs]
ys_real = [abs(math.pi-i) for i in arr_pi]
#print("k = " + str(k) + " n = " + str(n), file = out)
#print(str(w*4) + " +- " + str(delta*4) + "; probability = 0.99", file = out)
#print("Difference = " + str(abs(w*4-math.pi)), file = out)
#print("Disp: " + str(n*math.pi/4*(1-math.pi/4)), file = out)
#print("End.\n", file = out)
out.close()
plt.plot(xs, ys, c = 'pink')
plt.scatter(xs, ys_real, marker="+", c = 'black')
plt.xscale('log')
plt.xlabel('Number of points')
plt.ylabel('Error')
#plt.title('Decrease of error relative to number of points')
plt.show()