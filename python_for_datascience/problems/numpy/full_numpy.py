import numpy as np
arr = np.full((3, 4), 3)
print(type(arr))

import numpy as np
arr = np.array([1, 6, 8, 3, 0, 5])
x = arr.sort()
print(x)

import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
arr = arr.reshape(2, 3, 2)
arr = arr.reshape(3, -1, 2)
print(arr.shape)


import numpy as np
arr = np.array([3, -1, 5, 2, 0, -4])
np.sort(arr)
print(arr)


import numpy as np
arr = np.array([1, 2, 3, 4])
result = np.sum([1, 2])
print(result)