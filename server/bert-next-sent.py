import torch
from transformers import BertTokenizer, BertForNextSentencePrediction

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
outputs = model(input_ids)
seq_relationship_scores = outputs[0]

print(seq_relationship_scores)
