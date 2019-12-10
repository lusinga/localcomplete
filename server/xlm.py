import torch

from transformers import XLMTokenizer, XLMWithLMHeadModel

tokenizer = XLMTokenizer.from_pretrained('xlm-mlm-17-1280')
model = XLMWithLMHeadModel.from_pretrained('xlm-mlm-17-1280')
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
outputs = model(input_ids)
last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple

print(last_hidden_states)
print(last_hidden_states.shape)
predicted_index = torch.argmax(last_hidden_states).item()
print(predicted_index)
predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])
print(predicted_token)
