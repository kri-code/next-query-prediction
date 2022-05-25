from lib2to3.pgen2.literals import test
import torch
from torch import nn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import hamming_loss, f1_score, accuracy_score
from sklearn.neighbors import DistanceMetric
import decode_dict as d
import encode_and_decode as decode

class RNN(nn.Module):
    def __init__(self, input_size=2032, output_size=2032, hidden_dim=256):
        super(RNN, self).__init__()

        # Defining some parameters
        self.hidden_dim = hidden_dim

        #Defining the layers
        self.i2h = nn.Linear(input_size + hidden_dim, hidden_dim)
        self.i2o = nn.Linear(input_size + hidden_dim, output_size)
        self.sigmoid = nn.Sigmoid()
        
    
    def forward(self, input_tensor, hidden_tensor):
        combined = torch.cat((input_tensor, hidden_tensor), 1)

        hidden = self.i2h(combined)
        out = self.i2o(combined)
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


test_input = [d.query_dict["21a"]]
test_target = [[d.query_dict["22a"]]]
print(len(d.query_dict["21a"]))

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

print(output_calc_int)