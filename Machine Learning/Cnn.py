from tensorflow import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dropout, Dense

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape the data for CNN compatibility
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Normalize pixel values to a range of 0 to 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Create a Sequential model
model = Sequential()

# Add a Convolutional Layer
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# Add a MaxPooling Layer
model.add(MaxPool2D((2, 2)))

# Add a Flatten Layer
model.add(Flatten())

# Add a Dense Layer
model.add(Dense(100, activation='relu'))

# Add the output Dense Layer
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10)