# -*- coding: utf-8 -*-
"""100%_NN_Pytorch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jz9cCf_zQEIdnA5GZdtiSsXn3gvNDj2I
"""

#Import Pytorch
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim

transform=transforms.Compose([transforms.ToTensor(),
                              transforms.Normalize((0.1307,),(0.3081,))])
train_dataset=datasets.MNIST('data',train=True,download=True,transform=transform)
train_loader=torch.utils.data.DataLoader(train_dataset,batch_size=64,shuffle=True)

class Neural(nn.Module):
  def __init__(self):
    super(Neural,self).__init__()
    self.fc1=nn.Linear(28*28,128)
    self.fc2=nn.Linear(128,32)
    self.fc3=nn.Linear(32,10)



  def forward(self,x):
    x=x.view(-1,28*28)
    x=torch.relu(self.fc1(x))
    x=torch.relu(self.fc2(x))
    x=self.fc3(x)
    return x
net=Neural()

criterion=nn.CrossEntropyLoss()
optimizer=optim.SGD(net.parameters(),lr=0.01,momentum=0.5)

num_epochs=10
for epoch in range(num_epochs):
  for batch_idx,(data,target) in enumerate (train_loader):
    optimizer.zero_grad()
    output=net(data)
    loss =criterion(output,target)
    loss.backward()
    optimizer.step()
    if batch_idx % 100==0:
      print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

test_dataset=datasets.MNIST('data',train=False,download=True,transform=transform)
test_loader=torch.utils.data.DataLoader(test_dataset,batch_size=1000,shuffle=True)
correct=0
total=0
with torch.no_grad():
  output=net(data)
  _,predicted=torch.max(output.data,1)
  total+=target.size(0)
  correct+=(predicted==target).sum().item()

print('Accuracy of the network on the 10000 test images: %d %%' % (
    100 * correct / total))

