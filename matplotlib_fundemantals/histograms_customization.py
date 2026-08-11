import matplotlib.pyplot as plt
import numpy as np

#np.random.normal(loc=Ortalama, scale=Standart Sapma, size=Boyut)
scores = np.random.normal(loc=80, scale=10, size=100000)

plt.hist(scores, bins=100,
                 color="green",
                 edgecolor="black")


plt.title("Normal Distribution")
plt.xlabel("Score", color="red")
plt.ylabel("Number of People", color="blue")
plt.show()