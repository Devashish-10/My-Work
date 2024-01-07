from sklearn.ensemble import RandomForestClassifier

class RandomForest:
    def __init__(self, n_estimators=100, max_depth=None, random_state=None):
             self.clf = RandomForestClassifier(
             n_estimators=n_estimators, max_depth=max_depth, random_state=random_state
        )

    def fit(self, X, y):
         self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict(X)

    def score(self, X, y):
         return self.clf.score(X, y) #accuracy


def main():
    #training
     from sklearn.datasets import load_iris

    # Load the Iris dataset.
     iris = load_iris()

    # Split the dataset into training and test sets.
     X_train, X_test, y_train, y_test = iris.data[:-25], iris.data[-25:], iris.target[:-25], iris.target[-25:]

    # Create a random forest classifier.
     rf = RandomForest()

    # Fit the random forest classifier to the training data.
     rf.fit(X_train, y_train)

    # Predict the labels for the test data.
     y_pred = rf.predict(X_test)

    # Calculate the accuracy of the classifier on the test data.
     accuracy = rf.score(X_test, y_test)

     print("Accuracy:", accuracy)


if __name__ == "__main__":
    main()