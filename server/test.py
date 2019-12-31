import torch

# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer_lm.wmt19.en', ...]

# Load an English LM trained on WMT'19 News Crawl data
en_lm = torch.hub.load('pytorch/fairseq', 'transformer_lm.wmt19.en', tokenizer='moses', bpe='fastbpe')

# Sample from the language model
print(en_lm.sample('Barack Obama', beam=1, sampling=True, sampling_topk=10, temperature=0.8))
# "Barack Obama is coming to Sydney and New Zealand (...)"
