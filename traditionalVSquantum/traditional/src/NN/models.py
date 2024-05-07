import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# Convert numpy arrays to torch tensors
inputs_tensor = torch.tensor(inputs, dtype=torch.float32)
labels_tensor = torch.tensor(labels, dtype=torch.long)

# Custom Dataset
class TSPDataset(Dataset):
    def __init__(self, inputs, labels):
        self.inputs = inputs
        self.labels = labels
    
    def __len__(self):
        return len(self.labels)
    
    def __getitem__(self, idx):
        return self.inputs[idx], self.labels[idx]

# Load data
dataset = TSPDataset(inputs_tensor, labels_tensor)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Model 1: Simple feedforward model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 128)
        self.fc2 = nn.Linear(128, num_cities)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.softmax(self.fc2(x), dim=1)
        return x

# Model 2: LSTM Model
class LSTMModel(nn.Module):
    def __init__(self):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(num_cities, 50)
        self.lstm = nn.LSTM(50, 64, batch_first=True)
        self.fc = nn.Linear(64, num_cities)
    
    def forward(self, x):
        x = self.embedding(x)
        x, _ = self.lstm(x)
        x = x[:, -1, :]  # Get last time step
        x = torch.softmax(self.fc(x), dim=1)
        return x

# Model 3: More complex LSTM Model
class ComplexLSTMModel(nn.Module):
    def __init__(self):
        super(ComplexLSTMModel, self).__init__()
        self.embedding = nn.Embedding(num_cities, 50)
        self.lstm1 = nn.LSTM(50, 128, batch_first=True, return_sequences=True)
        self.lstm2 = nn.LSTM(128, 64, batch_first=True)
        self.fc = nn.Linear(64, num_cities)
    
    def forward(self, x):
        x = self.embedding(x)
        x, _ = self.lstm1(x)
        x, _ = self.lstm2(x)
        x = x[:, -1, :]  # Get last time step
        x = torch.softmax(self.fc(x), dim=1)
        return x

# Example of setting up one model
model = SimpleNN()
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Training loop for one model
def train_model(model, dataloader):
    model.train()
    for epoch in range(10):  # number of epochs
        for data, target in dataloader:
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Train the model
train_model(model, dataloader)
