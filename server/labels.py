import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
model = model.to('cuda')

inputs = "let disposable_begin_buffer = vscode.commands.registerCommand('extension.littleemacs.beginningOfBuffer',\nmove.beginningOfBuffer);\nlet disposable_end_buffer = vscode.commands."

tokens = tokenizer.tokenize(inputs)
print(tokens)

token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(token_ids)

input_ids = torch.tensor(tokenizer.encode(inputs)).unsqueeze(0)  # Batch size 1
input_ids = input_ids.to('cuda')
outputs = model(input_ids, labels=input_ids)
loss, logits = outputs[:2]
print(loss)
print(logits)

num_added_toks = tokenizer.add_tokens(['new_tok1', 'my_new-tok2'])
print('We have added', num_added_toks, 'tokens')
model.resize_token_embeddings(len(tokenizer))

special_tokens_dict = {'cls_token': '<CLS>'}
num_added_toks = tokenizer.add_special_tokens(special_tokens_dict)
print('We have added', num_added_toks, 'tokens')
model.resize_token_embeddings(len(tokenizer))
print(tokenizer.cls_token)

#tokenizer.save_pretrained("./save/")
#tokenizer.save_vocabulary('./save2')