import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits", "Vegetable","Tools"])
values = np.array([1,5,6,9])

plt.bar(categories, values, color="red")
#yatay bar çizdirmek için
#plt.barh(categories, values, color="red")



plt.title("Consumption", fontsize=20)
plt.xlabel("Food", fontsize=20)
plt.ylabel("Quantity", fontsize=20)

plt.show()