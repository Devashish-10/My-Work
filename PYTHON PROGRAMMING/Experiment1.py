import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases for the hidden and output layers
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, X):
        # Forward propagation
        self.hidden_layer_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.predicted_output = self.sigmoid(self.output_layer_input)
        return self.predicted_output

    def backward(self, X, y, output):
        # Backpropagation
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoid_derivative(output)

        self.hidden_layer_error = self.output_delta.dot(self.weights_hidden_output.T)
        self.hidden_layer_delta = self.hidden_layer_error * self.sigmoid_derivative(self.hidden_layer_output)

        self.weights_hidden_output += self.hidden_layer_output.T.dot(self.output_delta)
        self.bias_output += np.sum(self.output_delta, axis=0, keepdims=True)
        self.weights_input_hidden += X.T.dot(self.hidden_layer_delta)
        self.bias_hidden += np.sum(self.hidden_layer_delta, axis=0, keepdims=True)

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            loss = np.mean(np.square(y - output))
            print(f"Epoch {epoch+1}/{epochs}, Loss: {loss:.4f}")

# Create a toy dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create a neural network instance
input_size = 2
hidden_size = 4
output_size = 1
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Train the neural network
epochs = 10000
nn.train(X, y, epochs)

# Test the neural network
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = nn.forward(test_data)
print("Predictions:")
print(predictions)
