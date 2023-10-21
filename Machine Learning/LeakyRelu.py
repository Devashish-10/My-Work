import numpy as np
import matplotlib.pyplot as plt

# Leaky Rectified Linear Unit (Leaky ReLU) function
def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Generate x values
x = np.linspace(-2, 2, 200)
y = leaky_relu(x)

# Plot the Leaky ReLU function
plt.plot(x, y)
plt.title('Leaky ReLU Function')
plt.xlabel('x')
plt.ylabel('leaky_relu(x)')
plt.grid(True)
plt.show()