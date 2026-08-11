import matplotlib.pyplot as plt
import numpy as np

x = np.array([2026,2027,2028,2029])
y = np.array([10,30,20,50])
y2 = np.array([17,20,64,72])


plt.plot(x, y, marker=".", markersize=10,      # bu özellikleri dict haline getirebiliriz
                          markerfacecolor="red",
                          markeredgecolor="blue",
                          linestyle="dashed",
                          linewidth=2,
                          color="black")

line_style = dict(marker=".",
                  markersize=10,      # bu özellikleri dict haline getirebiliriz
                  markerfacecolor="red",
                  markeredgecolor="blue",
                  linestyle="dashed",
                  linewidth=2,
                  color="black")

plt.plot(x, y2, **line_style) #**keyword argument
plt.show()
