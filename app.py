from flask import Flask, request, jsonify
from logic import three_sum

app = Flask(__name__)

@app.route('/three-sum', methods=['POST'])
def solve():
    data = request.json
    nums = data['nums']
    return jsonify(three_sum(nums))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
