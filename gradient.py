# -*- coding: utf-8 -*-
"""gradient.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y9G7Q2ZHEnbgk3l58u_vESPRiibivjla
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv('https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/train.csv')
test=pd.read_csv("https://raw.githubusercontent.com/ezioauditore-tech/AI/main/datasets/Titanic/test.csv")

test.isnull().sum()

train.info(),test.info()

train.set_index("PassengerId",inplace=True)
test.set_index("PassengerId",inplace=True)

train



y_train=train["Survived"]

train.drop(labels="Survived",axis=1,inplace=True)

train.shape

train_test=train.append(test)
 #coz data are very lil we also add test data to it therefore, we combine test and train

col_drop=["Name","Age","SibSp","Ticket","Parch","Cabin","Embarked"]
train_test.drop(labels=col_drop,axis=1,inplace=True)

train_test_dummies=pd.get_dummies(train_test,columns=["Sex"]) #get dummies is used for one hot encoder

train_test_dummies.shape

train_test_dummies.isnull().sum()

train_test_dummies.fillna(value=0.0,inplace=True)

x_train=train_test_dummies.values[0:891] #to separate train and test
x_test=train_test_dummies.values[891:]

from sklearn.preprocessing import MinMaxScaler
scaler =MinMaxScaler()
x_train_scale=scaler.fit_transform(x_train)
x_test_scale=scaler.transform(x_test)

from sklearn.model_selection import train_test_split

x_train_sub,x_valid_sub,y_train_sub,y_valid_sub=train_test_split(x_train_scale,y_train,random_state=0)

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,confusion_matrix

learning_rate=[0.05,0.75,0.1,0.25,0.5,1]
for learning_rate in learning_rate:
  gb=GradientBoostingClassifier(n_estimators=20,learning_rate=learning_rate,max_features=2, max_depth=2, random_state=0)
  gb.fit(x_train_sub,y_train_sub)
  print("Learning rate: ",learning_rate)
  print("Accuracy scaore(train): {0:3f}".format(gb.score(x_train_sub,y_train_sub)))
  print("Accu score (validation): {0:3f}".format(gb.score(x_valid_sub,y_valid_sub)))
  print()

