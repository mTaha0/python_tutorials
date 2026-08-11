import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["elma", "armut", "karpuz", "vişne","kiraz"])
values = np.array([200, 300, 500, 800, 150])
colors = ["red", "yellow", "green", "gray","black"]

plt.pie(values, labels=categories, 
                autopct="%1.1f", 
                colors=colors, 
                explode=[0.1, 0.1, 0.1, 0.1, 0.1],
                shadow=True) #startangel=90 ile tablo döndürülebilir.

plt.show()