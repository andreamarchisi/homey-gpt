from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/gpt-endpoint', methods=['GET'])
def gpt_endpoint():
    app.logger.info("Endpoint /gpt-endpoint was called")
    return jsonify({"message": "Hello, Homey GPT!"})

if __name__ == '__main__':
    app.logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
