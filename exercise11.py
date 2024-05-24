"""
import numpy as np

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

a = np.arange(1, 13)
a3d = a.reshape(3, 2, 2)

###
folgende eigenschaften des 3d arrays kann man mit diesen operationen im interaktiven modus abfragen:
a3d.ndim
a3d.shape
a3d.size
a3d.dtype
###

print(a3d)
"""

import numpy as np

b = np.identity(5, dtype = "int")

b[3:, :2] = 2
b[:2, 3:] = 3

print(b)