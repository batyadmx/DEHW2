import numpy as np

array = np.load("matrix_99_2.npy")
X = []
Y = []
Z = []

for (x,y), z in np.ndenumerate(array):
    if z >= 599:
        X.append(x)
        Y.append(y)
        Z.append(z)

np.savez("uncompressed.npz", x = X, y = Y, z = Z)
np.savez_compressed("compressed.npz", x = X, y = Y, z = Z)