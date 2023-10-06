# =============================================================================
# NumPy Data Sheet
# =============================================================================

# =============================================================================
# Import NumPy Library
# =============================================================================
import numpy as np

# =============================================================================
# 1D Arrays
# =============================================================================

# Explanation: Creating a 1D array using NumPy
# A 1D array is essentially a list of numbers.
one_d_array = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {one_d_array}")

# Methods You Can Use with 1D Arrays
# 1. Shape: To find the dimensions
print(f"Shape: {one_d_array.shape}")

# 2. Sum: Adds up the elements
print(f"Sum: {one_d_array.sum()}")

# 3. Mean: Finds the mean
print(f"Mean: {one_d_array.mean()}")

# 4. Max and Min: Finds the maximum and minimum
print(f"Max: {one_d_array.max()}, Min: {one_d_array.min()}")

# =============================================================================
# 2D Arrays
# =============================================================================

# Explanation: Creating a 2D array (matrix) using NumPy
# A 2D array is like a list of lists, generally used to represent a matrix.
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array:\n {two_d_array}")

# Methods You Can Use with 2D Arrays
# 1. Shape: To find the dimensions
print(f"Shape: {two_d_array.shape}")

# 2. Reshape: To change the dimensions
reshaped = two_d_array.reshape(1, 9)
print(f"Reshaped:\n {reshaped}")

# 3. Dot: Matrix multiplication
print(f"Dot Product:\n {np.dot(two_d_array, two_d_array)}")

# =============================================================================
# 3D Arrays
# =============================================================================

# Explanation: Creating a 3D array using NumPy
# A 3D array is like a list of matrices.
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3D Array:\n {three_d_array}")

# Methods You Can Use with 3D Arrays
# 1. Shape: To find the dimensions
print(f"Shape: {three_d_array.shape}")

# =============================================================================
# Numerical Functions
# =============================================================================

# Explanation: NumPy has a range of built-in mathematical functions for fast operations.

# 1. Sine: np.sin
print(f"Sine: {np.sin(np.pi/2)}")

# 2. Cosine: np.cos
print(f"Cosine: {np.cos(np.pi)}")

# 3. Exponential: np.exp
print(f"Exponential: {np.exp(1)}")

# 4. Square root: np.sqrt
print(f"Square Root: {np.sqrt(4)}")

# 5. Logarithm: np.log
print(f"Natural Log: {np.log(2.71828)}")

# =============================================================================
# Explanations and Use Cases
# =============================================================================

# 1. 1D Arrays: Use for simple lists of numbers.
# 2. 2D Arrays: Use for matrices and matrix operations.
# 3. 3D Arrays: Use for 3D data or nested matrices.
# 4. Numerical Functions: Use for fast mathematical operations on arrays.

# This data sheet should offer a broad understanding of how to manipulate arrays and perform mathematical operations using NumPy.
