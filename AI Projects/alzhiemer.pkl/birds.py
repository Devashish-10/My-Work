import numpy as np
import pandas as pd
import tensorflow as tf
import os
from keras.layers import Conv2D,MaxPool2D,Dense, Flatten
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.metrics import classification_report,confusion_matrix
dataset="C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/PYTHON PROJECT/Bird Project"
dataset_train=os.path.join(dataset,'train')
dataset_test=os.path.join(dataset,'test')
img_height,img_width=224,224
epochs=25
batch_size=32
num_classes=525
train_data_augment=ImageDataGenerator(rescale=1.0/255.0,rotation_range=20,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')
test_data_augment=ImageDataGenerator(rescale=1.0/255.0)
train_data_gen=train_data_augment.flow_from_directory(
    dataset_train,
    target_size=(224,224),
    batch_size=batch_size,
    class_mode='categorical'
)
test_data_gen=train_data_augment.flow_from_directory(
    dataset_test,
    target_size=(224,224),
    batch_size=batch_size,
    class_mode='categorical'
)
model=Sequential()
model.add(Conv2D(64,(3,3),activation='relu',input_shape=(img_height,img_width,3)))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(128,(3,3),activation='relu'))
model.add(MaxPool2D((2,2)))
model.add(Conv2D(256,(3,3),activation='relu'))
model.add(MaxPool2D((2,2)))
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dense(num_classes,activation='softmax'))
model.compile(optimizer=Adam(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(train_data_gen,epochs=epochs)
loss,accuracy=model.evaluate(test_data_gen)
print("Test Loss: ",loss)
print("Test Accuracy: ",accuracy)
y_pred=model.predict(test_data_gen)
y_pred_classes=np.argmax(y_pred,axis=1)
y_true_classes=test_data_gen.classes
class_label=list(test_data_gen.class_indices.keys())
print("Classification Report: \n")
print(classification_report(y_true_classes,y_pred_classes,target_names=class_label))
print("Confusion Matrix:\n")
print(confusion_matrix(y_true_classes,y_pred_classes))
model.save("C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/PYTHON PROJECT/Birds.pkl")

