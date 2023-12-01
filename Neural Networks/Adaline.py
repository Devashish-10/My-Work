import numpy as np

class Adaline:
    def __init__(self, learning_rate=0.01, num_epochs=100):
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.cost_history = []

        for _ in range(self.num_epochs):
            output = self.net_input(X)
            errors = (y - output)
            self.weights[1:] += self.learning_rate * X.T.dot(errors)
            self.weights[0] += self.learning_rate * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_history.append(cost)

        return self

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

if __name__ == '__main__':
   
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([1, -1, -1, 1])

    # Create and train the Adaline model
    adaline = Adaline(learning_rate=0.01, num_epochs=100)
    adaline.fit(X_train, y_train)

    # Make predictions on new data
    X_new = np.array([[5, 6], [1, 1]])
    predictions = adaline.predict(X_new)

    print("Predictions:", predictions)