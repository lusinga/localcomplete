from flask import Flask
from flask import request
import json
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import time
from model_status import ModelStatus


def single_process_code(text):
    begin = time.time()
    # 输入待补全的文本

    # 以上次预测结果作为本次的输入，所谓的自回归
    indexed_tokens = tokenizer.encode(text)

    # 将读出的索引标记转化成PyTorch向量
    tokens_tensor = torch.tensor([indexed_tokens])

    # 设置为eval模式，这样就不会执行训练模式下的Dropout过程
    model.eval()

    # 使用GPU进行加速，诚实地讲速度不太快
    #tokens_tensor = tokens_tensor.to('cuda')

    # 进行推理
    with torch.no_grad():
        outputs = model(tokens_tensor)
        predictions = outputs[0]

        # 获取预测的下一个子词
    predicted_index = torch.argmax(predictions[0, -1, :]).item()
    # 解码成我们都读懂的文本
    predicted_text = tokenizer.decode([predicted_index])
    # 打印输入结果
    # print(predicted_text)
    result = (text + predicted_text)
    #predicted_text = predicted_text + ""
    print(result)
    print(time.time()-begin)
    return result


def process_code(text, is_cuda):
    begin = time.time()

    predicted_text = text

    # 每一个只能补一个token出来，补一句话需要多次，30次是我拍脑袋的
    for i in range(0, 1):

        # 以上次预测结果作为本次的输入，所谓的自回归
        indexed_tokens = tokenizer.encode(predicted_text)

        # 将读出的索引标记转化成PyTorch向量
        tokens_tensor = torch.tensor([indexed_tokens])

        # 设置为eval模式，这样就不会执行训练模式下的Dropout过程
        model.eval()

        # 使用GPU进行加速，诚实地讲速度不太快
        if is_cuda:
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
    print(time.time()-begin)
    return predicted_text


# TODO: Fast engine
def fast_engine(text):
    return '<BUSY>'


app = Flask(__name__)
m_status = ModelStatus()


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
    print('Post is ' + code2.get('code'))
    # return single_process_code(code2.get('code'))
    global m_status
    global CUDA
    status = m_status.check()
    result = ''
    if not status:
        result = process_code(code2.get('code'),CUDA)
        m_status.finish()
    else:
        result = fast_engine(code2.get('code'))
    return result


CUDA = False
# MODEL = '/workspace/xulun/out4/'
MODEL = '/workspace/xulun/out_banmalite/'

# 加载词汇表
tokenizer = GPT2Tokenizer.from_pretrained(MODEL)

# 加载模型中预训练好的权值
model = GPT2LMHeadModel.from_pretrained(MODEL)
if CUDA:
    model.to('cuda')

app.run(host='0.0.0.0', port=30000, debug=True)
