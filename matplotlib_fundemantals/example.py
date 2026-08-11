import matplotlib.pyplot as plt
import numpy as np

#ekrana random sayılardan oluşan 100x100 bir matrisi siyah-beyaz bir resim olarak yazdıralım.
rng = np.random.default_rng()


matris = rng.integers(low=0, high=256, size=(100,100)) #size=oluşturacağımız matrisin şeklini belirtir

plt.imshow(matris, cmap="gray")
plt.axis("off")
plt.show()