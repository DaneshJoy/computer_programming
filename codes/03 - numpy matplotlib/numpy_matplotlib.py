import numpy as np
import matplotlib.pyplot as plt


# ## Numpy ndarray
my_arr = np.array([1, 2, 3, 4, 5])
print(my_arr * 2)
print(type(my_arr))

# ## Get array properties
print(my_arr.ndim)
print(my_arr.shape)
print(my_arr.dtype)

# ## More dimentions
my_arr2 = np.array([[1, 2, 3, 4, 5]])
print(my_arr2.shape)

my_arr3 = np.array([[1, 2, 3],
                    [4, 5, 6]])
print(my_arr3.shape)
print(my_arr3)

# ## Vector operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 2])

item_product = np.multiply(arr1, arr2)
# item_product = arr1 * arr2
dot_product = np.dot(arr1, arr2)
# dot_product = arr1 @ arr2
cross_product = np.cross(arr1, arr2)
print("Item product:", item_product)
print("Dot product:", dot_product)
print("Cross product:", cross_product)

# ## Create zeros/ones/random ndarrays
zeros = np.zeros([2, 3])
print(zeros)

ones = np.ones([2, 3, 2])
print(ones)
print(ones.shape)

x = np.random.normal(size=(2, 3))
print(x)
x.round(2)

# ## Matrice operations
mat1 = np.array([[1, 2, 3],
                 [1, 2, 3]])
mat2 = np.array([[2, 2, 2],
                 [2, 2, 2]])

item_product = np.multiply(mat1, mat2)
# item_product = mat1 * mat2
mat_multiplication = np.matmul(mat1, np.transpose(mat2))
# mat_multiplication = mat1 @ np.transpose(mat2)
print("Item product:\n", item_product)
print("Matrix multiplication:\n", mat_multiplication)

# ## Create a sinusoidal signal
x = np.linspace(0, 2*np.pi, 1000)
print(x.shape)

y1 = np.sin(x)
print(y1.shape)

# ## Plot the signal
plt.figure(figsize=(3, 2))
plt.plot(y1)
plt.show()

plt.figure(figsize=(3, 2))
plt.plot(x, y1)
plt.show()

y2 = -np.cos(x) + 1
plt.figure(figsize=(3, 2))
plt.plot(x, y2)
plt.show()

# ## Plot multiple signals
# colors: r, g, b, c, m, y, k
# styles: - | -- | -. | : | 
plt.figure(figsize=(5, 3))
plt.plot(x, y1, 'm-.', label='sin(x)')
plt.plot(x, y2, 'g:', label='-cos(x)+1')
plt.title('My signals')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.legend()
plt.show()

# Save figure
plt.savefig('waves.png', transparent=True, facecolor ="b", edgecolor ='m')
plt.savefig('waves.pdf', facecolor ="b", edgecolor ='m')
