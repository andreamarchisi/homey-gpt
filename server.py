from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/gpt-endpoint', methods=['GET'])
def gpt_endpoint():
    return jsonify({"message": "Hello, Homey GPT!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
