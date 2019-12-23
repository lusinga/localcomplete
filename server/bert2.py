import torch
from transformers import BertTokenizer, BertModel

import logging
logging.basicConfig(level=logging.INFO)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
outputs = model(input_ids)
last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple

print(last_hidden_states)
print(last_hidden_states.shape)
