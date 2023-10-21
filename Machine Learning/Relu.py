import numpy as np
import matplotlib.pyplot as plt

# Rectified Linear Unit (ReLU) function
def relu(x):
    return np.maximum(0, x)

# Generate x values
x = np.linspace(-2, 2, 200)
y = relu(x)

# Plot the ReLU function
plt.plot(x, y)
plt.title('ReLU Function')
plt.xlabel('x')
plt.ylabel('relu(x)')
plt.grid(True)
plt.show()