from lib2to3.pgen2.literals import test
from locale import normalize
import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import hamming_loss, f1_score, accuracy_score
from sklearn.neighbors import DistanceMetric
import decode_dict as d
import encode_and_decode as decode
from net import data

seen_queries = [] # target queries seen during training
for i in data:
    seen_queries.append(i[1])

class RNN(nn.Module):
    def __init__(self, input_size=2032, output_size=2032, hidden_dim=256):
        super(RNN, self).__init__()

        # Defining some parameters
        self.hidden_dim = hidden_dim

        #Defining the layers
        self.i2h = nn.Linear(input_size + hidden_dim, hidden_dim)
        self.i2o = nn.Linear(input_size + hidden_dim, output_size)
        self.sigmoid = nn.Sigmoid()
        self.dropout = nn.Dropout(p=0.25)
    
    def forward(self, input_tensor, hidden_tensor):
        combined = torch.cat((input_tensor, hidden_tensor), 1)

        hidden = self.i2h(combined)
        out = self.i2o(combined)
        #out = self.dropout(out)
        out = self.sigmoid(out)
        
        return out, hidden
    
    def init_hidden(self):
        # This method generates the first hidden state of zeros which we'll use in the forward pass
        # We'll send the tensor holding the hidden state to the device we specified earlier as well
        hidden = torch.zeros(1, self.hidden_dim)
        return hidden

predicter = RNN()

# Load trained NeuralNet
predicter.load_state_dict(torch.load('rnn_net.pt'))
predicter.eval()


test_input = [d.query_dict["1b"]]
test_tar = [d.query_dict["2b"]] # for checking output
test_target = [[d.query_dict["2b"]]]
print(len(d.query_dict["2b"]))

test_input_tensor = np.array(test_input)
test_target_tensor = np.asarray(test_target)

test_input_tensor = torch.from_numpy(test_input_tensor)
test_target_tensor = torch.from_numpy(test_target_tensor)

hidden = predicter.init_hidden()
output, _ = predicter(test_input_tensor, hidden)

output_calc = output
output_calc[output_calc >= 0.5] = 1
output_calc[output_calc < 0.5] = 0
output_calc_int = [int(i) for i in output_calc[0].tolist()]    # float to int

###############################################################################
#
# Get final prediction
#
###############################################################################
if output_calc_int in test_tar:
    print("YES")
    prediction = output_calc_int
else:
    nearest = []
    print(len(seen_queries))
    for seen in seen_queries:
        nearest.append(accuracy_score(seen, output_calc_int, normalize=False))
    print(nearest)
    # find 5 nearest neighbours
    nearest = np.array(nearest)
    max_indices = np.argpartition(nearest,-5)[-5:] # indices of 5 largest values 
    print(max_indices)
    seen_queries = np.array(seen_queries)
    five_nearest = seen_queries[max_indices]
    print("5", five_nearest)
    # loss for each of the 5 nearest neighbours
    loss_five_nearest = []
    criterion = nn.BCELoss()
    for five in five_nearest:
        loss_five_nearest.append(hamming_loss(five, output_calc_int))
    min_loss_indice = np.argmin(np.array(loss_five_nearest)) # indice of min loss values
    print(loss_five_nearest)
    # final prediction (lowest loss of nearest neighbour from already seen queries)
    prediction = seen_queries[min_loss_indice]

# check
hamming = hamming_loss(d.query_dict["2b"], prediction)
print(hamming)
acc_score = accuracy_score(d.query_dict["2b"], prediction, normalize=False)
print(acc_score)
