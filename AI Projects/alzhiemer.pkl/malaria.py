import os
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D,MaxPool2D,Flatten,Dense
from keras.optimizers import Adam
from sklearn.metrics import classification_report,confusion_matrix
from PIL import Image
data="C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/Malaria Cells"
data_train=os.path.join(data,"training_set")
data_test=os.path.join(data,"testing_set")
newdatatrain=os.path.join(data,"resize_train")
newdatatest=os.path.join(data,"resize_test")
def resize_images(dataset,newdataset,target_size):
     if not os.path.exists(newdataset):
          os.makedirs(newdataset)
     for file in os.listdir(dataset):
          dataset=os.path.join(dataset,file)
          newdataset=os.path.join(newdataset,file)
          if os.path.isfile(dataset):
               try:
                   img=Image.open(dataset)
                   img.resize(target_size,Image.ANTIALIAS)
                   img.save(newdataset)
               except:
                    print("An error occured")
resize_images(data_train,newdatatrain,(224,224))
batch_size=32
epochs=10
num_classes=2
img_height,img_width=224,224
train_data_aug=ImageDataGenerator(rescale=1.0/255.0,rotation_range=20,height_shift_range=0.2,width_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')
test_data_aug=ImageDataGenerator(rescale=1.0/255.0)
train_datagen=train_data_aug.flow_from_directory(newdatatrain,target_size=(img_height,img_width),batch_size=batch_size,class_mode='categorical')
train_datagen=train_data_aug.flow_from_directory(newdatatest,target_size=(img_height,img_width),batch_size=batch_size,class_mode='categorical')
model=Sequential()
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(img_height,img_width,3)))
model.add(MaxPool2D(2,2))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPool2D(2,2))
model.add(Conv2D(128,(3,3),activation='relu'))
model.add(MaxPool2D(2,2))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(num_classes,activation='softmax'))
model.fit(train_datagen,epochs=epochs)

