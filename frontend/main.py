import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins":"*"}}, send_wildcard=True)


API_URL = "https://project-iprj65656207932e507bae89718f-5000.preview.node01.inscode.run/image/generations"
headers = {
    # 请前往 https://aistudio.baidu.com/index/accessToken 查看 访问令牌
    "Authorization": "token da026271adac92edca187a86bd3e6abc3d13f203",
    "Content-Type": "application/json"
}


def query(payload):
    print(payload)
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response)
    return response.json()


@app.route('/')
def hello():
    return 'hello!'

@app.route('/image/generations', methods=['POST'])
def generation():
    data = request.json
    print(data)
    n = data.get('n')
    prompt = data.get('prompt')
    size = data.get('size')
    steps = data.get('steps')
    print(prompt)

    return query({
        'seed': random.randint(100000, 999999999),
        'n': n,
        'prompt': prompt,
        'size': size,
        'steps':steps
      })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
