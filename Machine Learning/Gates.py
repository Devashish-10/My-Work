import numpy as np

# Define the activation function (step function)
def step_function(x):
    return np.where(x > 0, 1, 0)

# Define the neural network model
class NeuralNetwork:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def feedforward(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        output = step_function(weighted_sum)
        return output

# Define the logical operations
def logical_and(x1, x2):
    nn = NeuralNetwork(2)
    nn.weights = np.array([0.5, 0.5])
    nn.bias = -0.7
    return nn.feedforward(np.array([x1, x2]))

def logical_or(x1, x2):
    nn = NeuralNetwork(2)
    nn.weights = np.array([0.5, 0.5])
    nn.bias = -0.2
    return nn.feedforward(np.array([x1, x2]))

def logical_nand(x1, x2):
    nn = NeuralNetwork(2)
    nn.weights = np.array([-0.5, -0.5])
    nn.bias = 0.7
    return nn.feedforward(np.array([x1, x2]))

def logical_nor(x1, x2):
    nn = NeuralNetwork(2)
    nn.weights = np.array([-0.5, -0.5])
    nn.bias = 0.2
    return nn.feedforward(np.array([x1, x2]))

def logical_xor(x1, x2):
    or_result = logical_or(x1, x2)
    nand_result = logical_nand(x1, x2)
    return logical_and(or_result, nand_result)

# Test the logical operations
print("Logical AND:")
print("0 AND 0 =", logical_and(0, 0))
print("0 AND 1 =", logical_and(0, 1))
print("1 AND 0 =", logical_and(1, 0))
print("1 AND 1 =", logical_and(1, 1))

print("\nLogical OR:")
print("0 OR 0 =", logical_or(0, 0))
print("0 OR 1 =", logical_or(0, 1))
print("1 OR 0 =", logical_or(1, 0))
print("1 OR 1 =", logical_or(1, 1))

print("\nLogical NAND:")
print("0 NAND 0 =", logical_nand(0, 0))
print("0 NAND 1 =", logical_nand(0, 1))
print("1 NAND 0 =", logical_nand(1, 0))
print("1 NAND 1 =", logical_nand(1, 1))

print("\nLogical NOR:")
print("0 NOR 0 =", logical_nor(0, 0))
print("0 NOR 1 =", logical_nor(0, 1))
print("1 NOR 0 =", logical_nor(1, 0))
print("1 NOR 1 =", logical_nor(1, 1))

print("\nLogical XOR:")
print("0 XOR 0 =", logical_xor(0, 0))
print("0 XOR 1 =", logical_xor(0, 1))
print("1 XOR 0 =", logical_xor(1, 0))
print("1 XOR 1 =", logical_xor(1, 1))