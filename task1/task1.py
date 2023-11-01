import numpy as np
import json

array = np.load("matrix_99.npy")
diag1 = np.diagonal(array)
diag2 = np.diagonal(array[::-1])

res = {
    "sum" : int(np.sum(array)),
    "avr" : float(np.average(array)),
    "sumMD" : int(np.sum(diag1)),
    "avrMD" : float(np.average(diag1)),
    "sumSD" : int(np.sum(diag2)),
    "avrSD" : float(np.average(diag2)),
    "max" : int(np.max(array)),
    "min" : int(np.min(array))
}

with open("result.txt", "w") as file:
    file.write(json.dumps(res))