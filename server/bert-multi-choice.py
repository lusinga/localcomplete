import torch
from transformers import BertTokenizer, BertForMultipleChoice

import logging
logging.basicConfig(level=logging.INFO)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMultipleChoice.from_pretrained('bert-base-uncased')
choices = ["Hello, my dog is cute", "Hello, my cat is amazing"]
input_ids = torch.tensor([tokenizer.encode(s) for s in choices]).unsqueeze(0)  # Batch size 1, 2 choices
labels = torch.tensor(1).unsqueeze(0)  # Batch size 1
outputs = model(input_ids, labels=labels)
loss, classification_scores = outputs[:2]

print(loss)
print(classification_scores)
