import requests
from flask import Flask, jsonify



API_URL = "https://bcr3p4q6s4a8ncp1.aistudio-hub.baidu.com/image/generations"
headers = {
    # 请前往 https://aistudio.baidu.com/index/accessToken 查看 访问令牌
    "Authorization": "token da026271adac92edca187a86bd3e6abc3d13f203",
    "Content-Type": "application/json"
}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "prompt":"杰作，高品质，超精细，全细节，8k"
})


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello!'

@app.route('/image/generations', methods=['GET'])
def generation():
    return query({
        'seed': 111,
        'n': 1,
        'prompt': '有一个人对着一头牛在弹琴',
      })

if __name__ == '__main__':
    app.run()
