import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


secret = mpimg.imread('test.bmp')
key = np.zeros(secret.shape, dtype=int)
key = np.random.randint(50, size=secret.size)
key = key.reshape(secret.shape )

e = secret^key    # encrypt

e = e^key         # decrypt

print(e)
print("---")
print(secret.shape)
plt.imshow(secret)
