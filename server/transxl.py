import torch
from transformers import TransfoXLTokenizer, TransfoXLLMHeadModel

tokenizer = TransfoXLTokenizer.from_pretrained('transfo-xl-wt103')
model = TransfoXLLMHeadModel.from_pretrained('transfo-xl-wt103')
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
outputs = model(input_ids)
prediction_scores, mems = outputs[:2]

_,n,_ = prediction_scores.shape
# print(n)
for i in range(n):
	predicted_index_i = torch.argmax(prediction_scores[0,i]).item()
	# print(predicted_index_i)
	predicted_token_i = tokenizer.convert_ids_to_tokens([predicted_index_i])[0]
	print(predicted_token_i)