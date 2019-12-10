from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained('gpt2')

generated = tokenizer.encode("let disposable_begin_buffer = vscode.commands.registerCommand(extension.littleemacs.beginningOfBuffer")
context = torch.tensor([generated])
past = None

for i in range(30):
    print(i)
    output, past = model(context, past=past)
    token = torch.argmax(output[0, :])

    generated += [token.tolist()]
    context = token.unsqueeze(0)

sequence = tokenizer.decode(generated)

print(sequence)
