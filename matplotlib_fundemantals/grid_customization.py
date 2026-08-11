import matplotlib.pyplot as plt
import numpy as np

x = np.array([2026,2027,2028,2029])
y = np.array([10,30,20,50])

plt.grid(axis="both",
         linewidth=2,
         color="gray",
         linestyle="dashed")

plt.xticks(x)
plt.yticks(y)

plt.plot(x, y)
plt.show()