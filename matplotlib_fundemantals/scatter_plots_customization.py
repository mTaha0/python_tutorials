import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1,2,3,4,4,5,6,7,8,9]) #hours studied
y1 = np.array([10,30,20,50,50,60,80,90,70,100]) #grades

x2 = np.array([1,2,3,4,4,5,6,7,8,9]) #hours studied
y2 = np.array([50,80,40,60,50,60,80,98,76,101]) #grades


plt.scatter(x1, y1, color="red",
                    alpha=0.5,
                    s = 200,
                    label= "Class A")

plt.scatter(x2, y2, color="blue",
                    alpha=0.5,
                    s = 200,
                    label= "Class B")


plt.title("Test Scores")
plt.xlabel("Hours")
plt.ylabel("Grade")

plt.legend()
plt.show()