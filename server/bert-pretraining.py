import torch
from transformers import BertTokenizer, BertForPreTraining

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForPreTraining.from_pretrained('bert-base-uncased')
input_ids = torch.tensor(tokenizer.encode("Hello,world")).unsqueeze(0)  # Batch size 1
outputs = model(input_ids)
prediction_scores, seq_relationship_scores = outputs[:2]

print(prediction_scores)
print(prediction_scores.shape)
print(prediction_scores[0,-1])
predicted_index = torch.argmax(prediction_scores[0,-1]).item()
print(predicted_index)
predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
print(predicted_token)
print(seq_relationship_scores)

_,n,_ = prediction_scores.shape
# print(n)
for i in range(n):
	predicted_index_i = torch.argmax(prediction_scores[0,i]).item()
	# print(predicted_index_i)
	predicted_token_i = tokenizer.convert_ids_to_tokens([predicted_index_i])[0]
	print(predicted_token_i)
