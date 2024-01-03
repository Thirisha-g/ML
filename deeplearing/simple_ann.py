# -*- coding: utf-8 -*-
"""simple_ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qMkR4L9s2hTREmNseFCkHxzRIV5IccA3
"""

import numpy as np

x=np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
x

y=np.array([[1],[0],[1]])
y

def sigmoid(x):
  return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
  return x*(1-x)

#learning rate: in grDIENT desecent , we update weights

epoch=5000
lr=0.1
input_neurons=x.shape[1]
hidden_neurons=3
output_neurons=1

# number of neurons in the input layer
#hidden_neurons = # number of neurons in the hidden layer
#output_neurons = # number of neurons in the output layer

wh=np.random.uniform(size=(input_neurons,hidden_neurons)) # Initializing weights for the connection between input layer and hidden layer

bh=np.random.uniform(size=(1,hidden_neurons)) # Initializing biases for the hidden layer

wo=np.random.uniform(size=(hidden_neurons,output_neurons))# Initializing weights for the connection between hidden layer and output layer

bo=np.random.uniform(size=(1,output_neurons))# Initializing biases for the output layer

for i in range(epoch):
  #forward
  hidden_input=np.dot(x,wh)
  hidden_input=hidden_input+bh
  hidden_activation=sigmoid(hidden_input)
  output_layer=np.dot(hidden_activation,wo)
  output=sigmoid(output_layer)
  #backward
  E=y-output
  slope_output=derivative_sigmoid(output)
  slope_hidden=derivative_sigmoid(hidden_activation)
  d_output=E*slope_output
  error_hidden=d_output.dot(wo.T)
  d_hidden=error_hidden*slope_hidden
  wo+=hidden_activation.T.dot(d_output)*lr
  bo+=np.sum(d_output,axis=0,keepdims=True)*lr
  wh+=x.T.dot(d_hidden)*lr
  bh+=np.sum(d_hidden,axis=0,keepdims=True)*lr

output
