# -*- coding: utf-8 -*-
"""pytorch_vs_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0xvYo4Zsv-QmixRk8Tx6Rufi53-uObt
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms  # Corrected typo in torchvision.transforms
from torchvision.datasets import MNIST
import tensorflow as tf
from torch.utils.data import DataLoader  # Corrected typo in DataLoader
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist  # Corrected typo in mnist
from tensorflow.keras.utils import to_categorical

# Rest of your code...

# Load and preprocess the MNIST dataset using PyTorch
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_dataset = MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Define the neural network using PyTorch
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

model_pt = Net()
criterion = nn.CrossEntropyLoss()
optimizer_pt = optim.Adam(model_pt.parameters(), lr=0.001)

import time
start_time_tf = time.time()
model_tf = models.Sequential()
model_tf.add(layers.Flatten(input_shape=(28, 28, 1)))
model_tf.add(layers.Dense(128, activation='relu'))
model_tf.add(layers.Dense(10, activation='softmax'))

model_tf.compile(optimizer='adam',
                 loss='categorical_crossentropy',
                 metrics=['accuracy'])

model_tf.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)
end_time_tf = time.time()

print(f"TensorFlow Training Time: {end_time_tf - start_time_tf} seconds")

start_time_pt = time.time()
for epoch in range(5):
    for images, labels in train_loader:
        optimizer_pt.zero_grad()
        outputs = model_pt(images.view(-1, 28 * 28))
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer_pt.step()
end_time_pt = time.time()
print(f"PyTorch Training Time: {end_time_pt - start_time_pt} seconds")

# Evaluation using TensorFlow
test_loss_tf, test_acc_tf = model_tf.evaluate(test_images, test_labels)
print(f"TensorFlow Test Accuracy: {test_acc_tf}")

# Evaluation using PyTorch
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model_pt(images.view(-1, 28 * 28))
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy_pt = correct / total
print(f"PyTorch Test Accuracy: {accuracy_pt}")

