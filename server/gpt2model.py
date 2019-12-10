import torch
from transformers import GPT2Tokenizer, GPT2Model

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
model.eval()
model = model.to('cuda')
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
input_ids = input_ids.to('cuda')
outputs = model(input_ids)
last_hidden_states = outputs[0] 
print(last_hidden_states.shape)
