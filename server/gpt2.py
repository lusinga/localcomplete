import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import numpy as np

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

# Load pre-trained model tokenizer (vocabulary)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

model = GPT2LMHeadModel.from_pretrained('gpt2')

model.eval()
model.to('cuda')

generated = tokenizer.encode(
    "let disposable_begin_buffer = vscode.commands.registerCommand('extension.littleemacs.beginningOfBuffer',\nmove.beginningOfBuffer);\nlet disposable_end_buffer = vscode.commands.")
token_context = torch.tensor([generated])
token_context = token_context.to('cuda')

past = None

for i in range(30):
    print(i)
    output, past = model(token_context, past=past)
    token = torch.argmax(output[0, :])

    generated += [token.tolist()]
    token_context = token.unsqueeze(0)
    token_context = token_context.to('cuda')
    past = past.to('cuda')


text2 = tokenizer.decode(generated)

# print(predicted_index)
#predicted_text = tokenizer.decode(indexed_tokens + [predicted_index])

# print(predicted_text)

#text2 = tokenizer.decode(top3.indices.cpu().numpy())
