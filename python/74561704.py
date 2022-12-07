import numpy as np

arr = np.array([1, 2])
lst = [np.array([1, 2]), np.array([3, 4]), None, None]

if list(arr) in [list(i) for i in lst if i is not None]:
    print("Yes")

else:
    print("No")
