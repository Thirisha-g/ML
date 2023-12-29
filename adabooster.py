# -*- coding: utf-8 -*-
"""adaBooster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gq-8Pa-YWzsCP0ZOqAKubIBD_QgklNc2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data
test = pd.read_csv("https://github.com/ezioauditore-tech/AI/raw/main/datasets/Titanic/test.csv")
train = pd.read_csv("https://github.com/ezioauditore-tech/AI/raw/main/datasets/Titanic/train.csv")

train.info(), test.info()

train.set_index("PassengerId", inplace=True)
test.set_index("PassengerId", inplace=True)

train

y_train = train["Survived"]

train.drop(labels="Survived", axis=1, inplace=True)

train.shape

train_test =  train.append(test)

columns_to_drop = ["Name", "Age", "SibSp", "Ticket", "Cabin", "Parch", "Embarked"]
train_test.drop(labels=columns_to_drop, axis=1, inplace=True)

train_test

train_test_dummies = pd.get_dummies(train_test, columns=["Sex"])

train_test_dummies.shape

train_test_dummies.isnull().sum()

train_test_dummies.fillna(value=0.0, inplace=True)

X_train = train_test_dummies.values[0:891]
X_test = train_test_dummies.values[891:]

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

# split training feature and target sets into training and validation subsets
from sklearn.model_selection import train_test_split

X_train_sub, X_valid_sub, y_train_sub, y_valid_sub = train_test_split(X_train_scale, y_train, random_state=0)

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix

gb=AdaBoostClassifier(n_estimators=20, random_state=0)
gb.fit(X_train_sub,y_train_sub)
print("Accuracy scaore(train): {0:3f}".format(gb.score(X_train_sub,y_train_sub)))
print("Accu score (validation): {0:3f}".format(gb.score(X_valid_sub,y_valid_sub)))
print()
