import torch
from transformers import AlbertTokenizer, AlbertForQuestionAnswering


tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
model = AlbertForQuestionAnswering.from_pretrained('albert-base-v2')
question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"
input_text = "[CLS] " + question + " [SEP] " + text + " [SEP]"
input_ids = tokenizer.encode(input_text)
token_type_ids = [0 if i <= input_ids.index(102) else 1 for i in range(len(input_ids))]
start_scores, end_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([token_type_ids]))
all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
print(' '.join(all_tokens[torch.argmax(start_scores) : torch.argmax(end_scores)+1]))
# a nice puppet