# =============================================================================
# Numerical Methods and Visualization Data Sheet
# =============================================================================

# =============================================================================
# Import Libraries
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# =============================================================================
# Solving Non-Linear Systems
# =============================================================================

# Explanation: 
# `fsolve` is used to find the roots of a non-linear system of equations.
# It employs numerical methods (like the Newton-Raphson method) to find the point where the function crosses zero.
# Below, we solve the equation x**2 - 4 = 0. The function crosses zero at x=2 and x=-2.

# The function whose roots we want to find
def equation(x):
    return x ** 2 - 4

# Initial guesses for the roots
initial_guesses = [1, -1]

# Finding the roots using fsolve
roots = fsolve(equation, initial_guesses)

print(f"Roots of the equation: {roots}")

# Use Cases:
# 1. Engineering problems where exact solutions cannot be found.
# 2. Real-world applications where the equations are complex and non-linear.

# =============================================================================
# Numerical Derivative
# =============================================================================

# Explanation: The derivative f'(x) is approximated by (f(x+h) - f(x-h)) / 2h
# Here, we calculate the derivative of x^2 at x=2.

h = 0.0001
x = 2
f_x = x ** 2
f_x_h = (x + h) ** 2
f_x_neg_h = (x - h) ** 2

numerical_derivative = (f_x_h - f_x_neg_h) / (2 * h)
print(f"Numerical derivative at x=2: {numerical_derivative}")

# =============================================================================
# Numerical Integral
# =============================================================================

# Explanation: The integral of f(x) from a to b is approximated by the trapezoidal rule
# Here, we integrate x^2 from 0 to 2.

a = 0
b = 2
N = 1000
dx = (b - a) / N

x_values = np.linspace(a, b, N)
y_values = x_values ** 2

numerical_integral = np.trapz(y_values, dx=dx)
print(f"Numerical integral of x^2 from 0 to 2: {numerical_integral}")

# =============================================================================
# Visualization with Matplotlib
# =============================================================================

# Explanation: Use Matplotlib to visualize functions and their derivatives/integrals
# Here, we plot x^2 and its numerical derivative

x_range = np.linspace(-3, 3, 100)
y_range = x_range ** 2
y_deriv = 2 * x_range  # Analytical derivative for comparison

plt.subplot(1, 2, 1)
plt.title('Function: f(x) = x^2')
plt.plot(x_range, y_range)

plt.subplot(1, 2, 2)
plt.title("Derivative: f'(x)")
plt.plot(x_range, y_deriv)

plt.tight_layout()
plt.show()

# =============================================================================
# Explanations and Use Cases
# =============================================================================

# 1. Non-linear Systems: Use for finding roots of equations.
# 2. Numerical Derivative: Use when an analytical derivative is hard to find.
# 3. Numerical Integral: Use for approximating the area under a curve.
# 4. Visualization: Use for visually interpreting and presenting your data and results.

