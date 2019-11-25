from flask import Flask
from flask import request
import json
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


def single_process_code(text):
        # 输入待补全的文本

        # 以上次预测结果作为本次的输入，所谓的自回归
    indexed_tokens = tokenizer.encode(text)

    # 将读出的索引标记转化成PyTorch向量
    tokens_tensor = torch.tensor([indexed_tokens])

    # 设置为eval模式，这样就不会执行训练模式下的Dropout过程
    model.eval()

    # 使用GPU进行加速，诚实地讲速度不太快
    tokens_tensor = tokens_tensor.to('cuda')

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
    return predicted_text


def process_code(text):

    # 将输入字符串编码
    indexed_tokens = tokenizer.encode(text)

    # 将读出的索引标记转化成PyTorch向量
    tokens_tensor = torch.tensor([indexed_tokens])

    # 设置为eval模式，这样就不会执行训练模式下的Dropout过程
    model.eval()

    # 使用GPU进行加速，诚实地讲速度不太快
    tokens_tensor = tokens_tensor.to('cuda')

    past = None

    # 每一个只能补一个token出来，补一句话需要多次，30次是我拍脑袋的
    for i in range(0,30):

        # 进行推理
        with torch.no_grad():
            outputs, past = model(tokens_tensor, past=past)
            token = torch.argmax(outputs[0, :])

            indexed_tokens += [token.tolist()]
            tokens_tensor = token.unsqueeze(0)

    predicted_text = tokenizer.decode(tokens_tensor)
    print(predicted_text)

    return predicted_text


app = Flask(__name__)


@app.route('/')
def index():
    print('index')
    return "<h1>It works!</h1>"


@app.route('/code/<code>')
def complete(code):
    print('Received code:%s' % code)
    return 'Hello, %s' % code


@app.route('/complete', methods=['POST'])
def code_complete():
    print('Received complete post')
    code = request.data.decode()
    code2 = json.loads(code)
    return single_process_code(code2.get('code'))


# 加载词汇表
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# 加载模型中预训练好的权值
model = GPT2LMHeadModel.from_pretrained('gpt2')
model.to('cuda')

app.run(port=30000, debug=True)