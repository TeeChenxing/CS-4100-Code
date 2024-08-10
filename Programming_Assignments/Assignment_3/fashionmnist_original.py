import torch
import torchvision
import torchvision.transforms.v2 as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

'''
In this file you will write end-to-end code to train a neural network to categorize fashion-mnist data
'''


'''
PART 1:
Preprocess the fashion mnist dataset and determine a good batch size for the dataset.
Anything that works is accepted.
'''

transform = transforms.Compose(''' Fill in this function ''')  # Use transforms to convert images to tensors and normalize them
batch_size = ''' Insert a good batch size number here '''

'''
PART 2:
Load the dataset. Make sure to utilize the transform and batch_size you wrote in the last section.
'''

trainset = torchvision.datasets.FashionMNIST(''' Fill in this function ''')
trainloader = torch.utils.data.DataLoader(''' Fill in this function ''')

testset = torchvision.datasets.FashionMNIST(''' Fill in this function ''')
testloader = torch.utils.data.DataLoader(''' Fill in this function ''')

'''
PART 3:
Design a neural network in PyTorch. Architecture is up to you, but please ensure that the model achieves at least 80% accuracy.
Do not directly import or copy any existing models from other sources, spend time tweaking things.
'''

class Net(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
        
net = Net()

'''
PART 4:
Choose a good loss function and optimizer
'''

criterion = ''' Find a good loss function '''
optimizer = ''' Choose a good optimizer and its hyperparamters '''

'''
PART 5:
Train your model!
'''

num_epochs = '''Choose the number of epochs '''

for epoch in range(num_epochs):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, '''Fill in the blank''')
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    print(f"Training loss: {running_loss}")

print('Finished Training')

torch.save(net.state_dict(), 'fmnist.pth')  # Saves model file (upload with submission)

'''
PART 6:
Evalute your model! Accuracy should be greater or equal to 80%

'''

correct = 0
total = 0
# since we're not training, we don't need to calculate the gradients for our outputs
with torch.no_grad():
    for data in testloader:
        ''' Fill in this section '''

print('Accuracy: ', correct/total)

'''
PART 7:
Check the written portion. You need to generate some plots. 
'''

'''

YOUR CODE HERE

'''