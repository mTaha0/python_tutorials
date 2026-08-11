import matplotlib.pyplot as plt
import numpy as np

x = np.array([2026,2027,2028,2029])
y = np.array([10,30,20,50])

plt.title("Class Size", fontsize=30,
                        family="Arial",
                        fontweight="bold",
                        color="gray")

plt.xlabel("Years",     fontsize=20,
                        family="Arial",
                        fontweight="bold",
                        color="blue")

plt.ylabel("Students", fontsize=20,
                            family="Arial",
                            fontweight="bold",
                            color="green")
plt.xticks(x)
plt.yticks(y)
plt.tick_params(axis="both",color="red")

plt.plot(x, y, marker=".")
plt.show()