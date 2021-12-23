import matplotlib.pyplot as plt
from math import sin
A =[]
j = 0
while j < 100:
    j+=1
    A.insert(j-1, j)
SA = [sin(i) for i in A]
plt.plot(SA)
plt.plot(range(100))
plt.show()