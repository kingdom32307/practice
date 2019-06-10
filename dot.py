import numpy as np

a = np.random.randint(0, 9, 5)
b = np.random.randint(0, 9, 5)
print(a)
print(b)
print(np.dot(a, b))

a = np.random.randint(0, 9, (3, 2))
b = np.random.randint(0, 9, (2, 3))
print(a)
print(b)
print(np.dot(a, b))
