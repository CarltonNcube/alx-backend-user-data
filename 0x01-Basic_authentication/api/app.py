#!/usr/bin/env python3
'''This script defines a simple Flask API with a status endpoint'''

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/status')
def status():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
