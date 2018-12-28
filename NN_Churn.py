# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:42:36 2018

@author: Kantshri B
"""

import numpy as np
import time
import datetime as dt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Documents/FTN_train.csv')

#handling dates

X = dataset.iloc[:, np.r_[2,5:6,7:24]].values
y = dataset.iloc[:,6].values
#y



#Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:,2] = labelencoder_X_2.fit_transform(X[:,2])

onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:,1:]


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#X_train[1:3,:]

import keras
from keras.models import Sequential
from keras.layers import Dense

#initialising NN
classifier = Sequential()
classifier.add(Dense(output_dim = 10, init='uniform', activation='relu', input_dim=19))
classifier.add(Dense(output_dim = 10, init='uniform', activation='relu'))
classifier.add(Dense(output_dim = 1, init='uniform', activation='sigmoid'))

#compiling the model
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#handling weights
classifier.fit(X_train, y_train, batch_size=15, nb_epoch=200)

#predicting churn
y_pred = classifier.predict(X_test)
y_pred_1 = (y_pred>0.75)
y_pred_2 = (y_pred>0.20)
y_pred_3 = (y_pred>0.95)
y_pred_4 = (y_pred>0.1)

#evaluating model
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test, y_pred_1)
cm2 = confusion_matrix(y_test, y_pred_2)
cm3 = confusion_matrix(y_test, y_pred_3)
cm4 = confusion_matrix(y_test, y_pred_4)
cm1
cm2
cm3
cm4









