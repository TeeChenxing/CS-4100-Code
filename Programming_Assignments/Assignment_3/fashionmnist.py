import matplotlib.pyplot as plt
import numpy as np

import torch
import torchvision

import torch.nn as nn
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

batch_size = 64
labels_map = {0: "T-Shirt",
              1: "Trouser",
              2: "Pullover",
              3: "Dress",
              4: "Coat",
              5: "Sandal",
              6: "Shirt",
              7: "Sneaker",
              8: "Bag",
              9: "Ankle Boot"}

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(nn.Linear(28*28, 512),
                                               nn.BatchNorm1d(512),
                                               nn.ReLU(),
                                               nn.Dropout(0.2),
                                               nn.Linear(512, 512),
                                               nn.BatchNorm1d(512),
                                               nn.ReLU(),
                                               nn.Dropout(0.2),
                                               nn.Linear(512, 10),)

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


def train_loop(dataloader, model, loss_fn, optimizer, loss_history):
    size = len(dataloader.dataset)
    model.train()
    running_loss = 0

    for batch, (images, labels) in enumerate(dataloader):
        # Compute prediction and loss
        pred = model(images)
        loss = loss_fn(pred, labels)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        running_loss += loss.item()

        if batch % 100 == 0:
            current = (batch * batch_size) + len(images) 
            loss_history.append(loss.item())  # Record the loss
            print(f"Training loss: {running_loss / (batch + 1):>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    model.eval()
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    accuracy = 100 * correct

    print(f"Test Accuracy: {accuracy:>0.1f}%, Avg loss: {test_loss:>8f} \n")

    return accuracy


def Q4(dataloader, model, directory):
    model.eval()
    
    correctly_classified = None
    incorrectly_classified = None
    
    with torch.no_grad():
        for images, labels in dataloader:
            preds = model(images)
            predicted_classes = preds.argmax(1)
            
            # Find first incorrect and correct classification
            for i in range(len(images)):
                if correctly_classified is None and predicted_classes[i] == labels[i]:
                    correctly_classified = (images[i], labels[i], predicted_classes[i])
                if incorrectly_classified is None and predicted_classes[i] != labels[i]:
                    incorrectly_classified = (images[i], labels[i], predicted_classes[i])
                
                # Break if both are found
                if correctly_classified and incorrectly_classified:
                    break

            if correctly_classified and incorrectly_classified:
                break

    # Plot and save the correctly classified image
    if correctly_classified:
        image, true_label, predicted_label = correctly_classified
        plt.style.use("dark_background")
        plt.figure()
        plt.imshow(image.squeeze(), cmap="gray")
        plt.title(f"Correctly Classified\n\nTrue: {labels_map[true_label.item()]}, Predicted: {labels_map[predicted_label.item()]}")
        plt.axis('off')
        plt.savefig(f"{directory}Q4_correct.png")

    # Plot and save the incorrectly classified image
    if incorrectly_classified:
        image, true_label, predicted_label = incorrectly_classified
        plt.style.use("dark_background")
        plt.figure()
        plt.imshow(image.squeeze(), cmap="gray")
        plt.title(f"Incorrectly Classified\n\nTrue: {labels_map[true_label.item()]}, Predicted: {labels_map[predicted_label.item()]}")
        plt.axis('off')
        plt.savefig(f"{directory}Q4_incorrect.png")


def plot_training_loss(loss_history, save_path):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 5))
    plt.plot(loss_history, color=(65/255, 105/255, 225/255))  # Use the user's preferred color
    plt.title("Training Loss Over Time")
    plt.xlabel("Batch")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.savefig(save_path)


def main():
    directory = "Programming_Assignments/Assignment_3/"
    figure_directory = "Problem_Sets/problem_set_3/"
    net = Net()

    training_data = torchvision.datasets.FashionMNIST(root=f"{directory}data", train=True, download=True, transform=ToTensor())
    test_data = torchvision.datasets.FashionMNIST(root=f"{directory}data", train=False, download=True, transform=ToTensor())

    train_dataloader = DataLoader(training_data, batch_size=batch_size)
    test_dataloader = DataLoader(test_data, batch_size=batch_size)

    learning_rate = 0.15
    epochs = 10

    # loss function and optimizer
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

    loss_history = []

    for epoch in range(epochs):
        print(f"Epoch {epoch + 1} \n-------------------------------")
        train_loop(train_dataloader, net, loss_fn, optimizer, loss_history)
        final_accuracy = test_loop(test_dataloader, net, loss_fn)

    print(f"Finished Training. Final Test Accuracy: {final_accuracy:.2f}%")

    # save model and plot
    torch.save(net.state_dict(), f"{directory}fmnist.pth")
    Q4(test_dataloader, net, figure_directory)
    plot_training_loss(loss_history, f"{figure_directory}Q5_training_loss.png")
    print("All Figures Saved Successfully")

if __name__ == "__main__":
    main()