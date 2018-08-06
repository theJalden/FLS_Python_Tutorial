import matplotlib.pyplot as plt
import math

x = [nn/100 for nn in range(1000)]
y = [math.sin(xx) for xx in x]

plt.plot(x, y)
plt.xlabel("Angle in Radians")
plt.ylabel("Sine")


plt.show()
