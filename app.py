# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return jsonify({
        'email':'testzasperqa@gmail.com',
        'name':'QaAdmin',
        'phno':1234567890,
        'message': 'Hello from Zasper Api'

        })

if __name__ == '__main__':
    app.run()
