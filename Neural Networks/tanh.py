import numpy as np
import matplotlib.pyplot as plt

# Hyperbolic Tangent (Tanh) function
def tanh(x):
    return np.tanh(x)

# Generate x values
x = np.linspace(-7, 7, 200)
y = tanh(x)

# Plot the Tanh function
plt.plot(x, y)
plt.title('Tanh Function')
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.grid(True)
plt.show()