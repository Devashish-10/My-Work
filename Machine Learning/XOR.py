import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights and biases
input_size = 2
hidden_size = 2
output_size = 1

np.random.seed(42)
weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))

bias_hidden = np.zeros((1, hidden_size))
bias_output = np.zeros((1, output_size))

learning_rate = 0.1
epochs = 10000

# Training loop
for epoch in range(epochs):
    # Forward propagation
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)
    output = sigmoid(np.dot(hidden_output, weights_hidden_output) + bias_output)

    # Calculate error
    error = y - output

    # Backpropagation
    d_output = error * sigmoid_derivative(output)
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights and biases
    weights_hidden_output += hidden_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden) * learning_rate
    bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# Testing the trained network
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
hidden_layer_input = np.dot(test_input, weights_input_hidden) + bias_hidden
hidden_layer_output = sigmoid(hidden_layer_input)
final_output = sigmoid(np.dot(hidden_layer_output, weights_hidden_output) + bias_output)
print(final_output)
