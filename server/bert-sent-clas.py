import torch
from transformers import BertTokenizer, BertForSequenceClassification

import logging
logging.basicConfig(level=logging.INFO)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
outputs = model(input_ids, labels=labels)
loss, logits = outputs[:2]

print(loss)
print(logits)
