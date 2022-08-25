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

seen_queries = [] # queries seen during training
for i in data:
    if i[0] not in seen_queries:
        seen_queries.append(i[0])
    if i[1] not in seen_queries:
        seen_queries.append(i[1])
print("LÄNGE GESEHEN:", len(seen_queries))

class lstm(nn.Module):
    def __init__(self, input_size, output_size, hidden_dim, n_layers, drop_prob=0.5):
        super(lstm, self).__init__()

        self.input_size = input_size
        self.output_size = output_size
        self.n_layers = n_layers
        self.hidden_dim = hidden_dim

        self.lstm = nn.LSTM(input_size, hidden_dim, n_layers, dropout=drop_prob, batch_first=True)

        self.dropout = nn.Dropout(drop_prob)
        self.fc = nn.Linear(hidden_dim, output_size)
        self.sigmoid = nn.Sigmoid()
    
    def init_state(self, batch_size):
        return (torch.zeros(self.n_layers, batch_size, self.hidden_dim),
                torch.zeros(self.n_layers, batch_size, self.hidden_dim))

    def forward(self, x, hidden):
        #batch_size = x.size(0)
        x = x.float()
        input = x
        print(input.size())
        
        hx, cx = self.init_state(1)

        lstm_out, hidden = self.lstm(input, (hx,cx))
        lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)
        
        out = self.dropout(lstm_out)
        #out = self.fc(lstm_out)
        out = self.fc(out)
        out = self.sigmoid(out)
        
        #out = out.view(batch_size, -1)
        #out = out[:,-1]
        return out, hidden
    
    def init_hidden(self):
        #weight = next(self.parameters()).data
        #hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_(),
                      #weight.new(self.n_layers, batch_size, self.hidden_dim).zero_())
        hidden = [torch.zeros(2, self.hidden_dim), torch.zeros(2, self.hidden_dim)]
        hidden = tuple(hidden)
        return hidden

input_size = 2032
output_size = 2032
hidden_dim = 268
n_layers = 2

predicter = lstm(input_size, output_size, hidden_dim, n_layers)

# Load trained NeuralNet
predicter.load_state_dict(torch.load('lstm_net.pt'))
predicter.eval()

print("TRAINED LSTM")
first_query = d.query_dict["1b"]
second_query = d.query_dict["2b"]

test_input = [[first_query]]
test_tar = [second_query] # for checking output
test_target = [[second_query]]
print(len(second_query))

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
    # find 3 nearest neighbours
    nearest = np.array(nearest)
    max_indices = np.argpartition(nearest,-3)[-3:] # indices of 3 largest values 
    print(max_indices)
    seen_queries = np.array(seen_queries)
    five_nearest = seen_queries[max_indices]
    print("5", five_nearest)
"""
# check
hamming = hamming_loss(d.query_dict["2b"], prediction)
print(hamming)
acc_score = accuracy_score(d.query_dict["2b"], prediction, normalize=False)
print(acc_score)"""

################################################################################
#
# decode
#
#################################################################################
actual = decode.decode_query(second_query)
actual_decode = []
for query, fragments in decode.result_dict.items():
    if actual == fragments:
        actual_decode.append(query)

for i in max_indices:
    query_fragments = decode.decode_query(seen_queries[i])
    for query, fragments in decode.result_dict.items():
        if query_fragments == fragments:
            if query in actual_decode:
                print(query)
                print(i, "LSTM")


