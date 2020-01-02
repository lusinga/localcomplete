import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# 加载词汇表
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# 输入待补全的文本
text = 'int idx = a.getIndex(i);\nfor (int i = 0; i < N; i++) {\nint attr = a.'
predicted_text = text

isCUDA = False

# 每一个只能补一个token出来，补一句话需要多次，30次是我拍脑袋的
for i in range(0,1):
    
    # 以上次预测结果作为本次的输入，所谓的自回归
    indexed_tokens = tokenizer.encode(predicted_text)

    # 将读出的索引标记转化成PyTorch向量
    tokens_tensor = torch.tensor([indexed_tokens])

    # 加载模型中预训练好的权值
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # 设置为eval模式，这样就不会执行训练模式下的Dropout过程
    model.eval()

    # 使用GPU进行加速，诚实地讲速度不太快
    if isCUDA:
        tokens_tensor = tokens_tensor.to('cuda')
        model.to('cuda')

    # 进行推理
    with torch.no_grad():
        outputs = model(tokens_tensor)
        predictions = outputs[0]

    # 获取预测的下一个子词
    predicted_index = torch.argmax(predictions[0, -1, :]).item()
    # 解码成我们都读懂的文本
    predicted_text = tokenizer.decode(indexed_tokens + [predicted_index])
    # 打印输入结果
    print(predicted_text)

    for i2 in range(2, 20):
        print(-i2)
        predicted_index2 = torch.argmax(predictions[0, -i2, :]).item()
        # 解码成我们都读懂的文本
        predicted_text2 = tokenizer.decode([predicted_index2])
        # 打印输入结果
        print(predicted_text2)
