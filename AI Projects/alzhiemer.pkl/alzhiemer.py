import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense 
from keras.optimizers import Adam
from sklearn.metrics import confusion_matrix,classification_report
data_lc="C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/Alzhiemer/Dataset"
batch_size=32
img_height,img_width=150,150
epochs=20
num_classes=4
train_datagen=ImageDataGenerator(
    rescale=1.0/255.0, 
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
)
test_datagen=ImageDataGenerator(rescale=1.0/255.0)
train_generator=train_datagen.flow_from_directory(
    data_lc,
    target_size=(img_height,img_width),
    batch_size=batch_size,
    class_mode='categorical',
)
test_generator=test_datagen.flow_from_directory(
    data_lc,
    target_size=(img_height,img_width),
    batch_size=batch_size,
    class_mode='categorical',
)
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_generator, epochs=epochs)
loss, accuracy = model.evaluate(test_generator)
print("Test loss:", loss)
print("Test accuracy:", accuracy)
y_pred = model.predict(test_generator)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = test_generator.classes
class_labels = list(test_generator.class_indices.keys())
print("Classification Report:")
print(classification_report(y_true_classes, y_pred_classes, target_names=class_labels))

print("Confusion Matrix:")
print(confusion_matrix(y_true_classes, y_pred_classes))
model.save("C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/PYTHON PROJECT/alzhiemer.pkl")

