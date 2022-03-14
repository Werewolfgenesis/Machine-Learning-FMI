import numpy as np

# Create a numpy from the list [7, 2, 9, 10]
arr = np.array([7, 2, 9, 10])
print(arr)


# 1. Create a vector of 10 zeros but the fifth value of which is 1
arr_temp = np.zeros(10)
arr_final = arr_temp + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
print(arr_final)

# 2. Create a vector with values ranging from 10 to 49 
arr_temp = np.array([i for i in range(10, 50)])
print(arr_temp)

# 3. Reverse an array in TWO ways
# The Python way:
arr_new = arr_temp[::-1]
print(arr_new) 

# with numpy function
arr_new = np.flip(arr_temp)
print(arr_new)

# 4. Create a 3x3 matrix with the values from 0 to 8
arr = np.array([i for i in range(0,9)])
arr_new = arr.reshape((3,3))
print(arr_new)

# 5. Find indices of non-zero elements
arr = np.array([1,2,0,0,4,0])
indices = np.where(arr != 0)
print(indices[0])

# 6. Create a 3x3 identity matrix
identity = np.identity(3)
print(identity)

# 7. Create a 3x3x3 array with random values drawn from the uniform distribution


