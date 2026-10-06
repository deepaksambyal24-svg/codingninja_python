
import numpy as np
data = np.array([10, 20, 30, 40, 50])
print(type(data))


matrix_x = np.array([[10, 20, 30, 40],
                     [50, 60, 70, 80],
                     [90, 100, 110, 120]])
matrix_y = matrix_x
print(matrix_y is matrix_x)

data = np.array([1.0, 2.9, 9+4j])
print(type(data[1]))

matrix = np.array(5, 10, 15, 20, 25, 30)
result = matrix % 7
print(result)


