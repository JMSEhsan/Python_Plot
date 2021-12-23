import matplotlib.pyplot as plt
from math import sin
A =[]
j = 0
k = 0
while j < 100:
    j+=1
    k+=0.3
    A.insert(j-1, k)
SA = [10*sin(i) for i in A]
plt.plot(SA)
plt.plot(range(100))
plt.show()