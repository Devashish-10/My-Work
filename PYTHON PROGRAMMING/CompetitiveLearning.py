import numpy as np

# Define the number of neurons and input dimensions
num_neurons = 4
input_dim = 2

# Initialize the weights randomly
weights = np.random.rand(num_neurons, input_dim)

# Define the learning rate
learning_rate = 0.1

# Define the input data
data = np.array([[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]])

# Define the number of epochs
epochs = 100

# Training the competitive learning network
for epoch in range(epochs):
    # Iterate through each input data point
    for input_point in data:
        # Calculate the Euclidean distance between input and weights
        distances = np.linalg.norm(weights - input_point, axis=1)
        
        # Find the winning neuron (the one with the minimum distance)
        winner_neuron = np.argmin(distances)
        
        # Update the weights of the winning neuron
        weights[winner_neuron] += learning_rate * (input_point - weights[winner_neuron])

# Print the final weights
print("Final Weights:")
print(weights)