import torch
from transformers import BertTokenizer, BertForMaskedLM

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
input_ids = torch.tensor(tokenizer.encode("#include <iostream>")).unsqueeze(0)  # Batch size 1
outputs = model(input_ids, masked_lm_labels=input_ids)
loss, prediction_scores = outputs[:2]

_,n,_ = prediction_scores.shape
# print(n)
for i in range(n):
	predicted_index_i = torch.argmax(prediction_scores[0,i]).item()
	# print(predicted_index_i)
	predicted_token_i = tokenizer.convert_ids_to_tokens([predicted_index_i])[0]
	print(predicted_token_i)
