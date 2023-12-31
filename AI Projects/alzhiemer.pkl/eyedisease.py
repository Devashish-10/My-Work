import numpy as np
import pandas as pd 
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D,MaxPool2D,Flatten,Dense 
from keras.optimizers import Adam
from sklearn.metrics import classification_report,confusion_matrix
dataset="C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/Eye Diseases"
batch_size=32
img_height,img_width=512,512
epochs=10
num_classes=4
train_data_aug=ImageDataGenerator(rescale=1.0/255.0,rotation_range=20,height_shift_range=0.2,width_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')
test_data_aug=ImageDataGenerator(rescale=1.0/255.0)
train_datagen=train_data_aug.flow_from_directory(dataset,target_size=(img_height,img_width),batch_size=batch_size,class_mode='categorical')
test_datagen=test_data_aug.flow_from_directory(dataset,target_size=(img_height,img_width),batch_size=batch_size,class_mode='categorical')
model=Sequential()
model.add(Conv2D(64,(2,2),activation='relu',input_shape=(img_height,img_width,3)))
model.add(MaxPool2D(2,2))
model.add(Conv2D(128,(2,2),activation='relu'))
model.add(MaxPool2D(2,2))
model.add(Conv2D(256,(2,2),activation='relu'))
model.add(MaxPool2D(2,2))
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dense(b=num_classes,activation='softmax'))
model.compile(optimizer=Adam(learning_rate=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(train_datagen,epochs=epochs)
loss,accuracy=model.evaluate(test_datagen)
print("Test Loss:",loss)
print("Test Accuracy :",accuracy)
y_pred=model.predict(test_datagen)
y_pred_classes=np.argmax(y_pred,axis=1)
y_true_classes=test_datagen.classes
class_label=list(test_datagen.class_indices.keys())
print("Classification Report:",classification_report(y_true_classes,y_pred_classes,target_names=class_label))
print("Confusion Matrix:",confusion_matrix(y_true_classes,y_pred_classes))
model.save("C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/PYTHON PROJECT/EyeDisease.pkl")
