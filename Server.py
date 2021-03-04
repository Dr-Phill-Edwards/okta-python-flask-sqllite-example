import os
import sqlite3
from flask import Flask, request, jsonify, abort
from okta_jwt.jwt import validate_token

app = Flask(__name__, static_url_path='', static_folder='client')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/<path:file>', methods=['GET'])
def serve_static(file):
    return app.send_static_file(file)

def verify():
    auth = request.headers.get('Authorization')
    if auth is None or not auth.startswith('Bearer '):
        abort(401, description="Authorization required")
    token = auth[7:]
    try:
        validate_token(token, os.environ['OKTA_ISSUER_URI'], 'api://default', os.environ['OKTA_CLIENT_ID'])
    except Exception as e:
        abort(403, "Unauthorized")

def readMessages():
    connection = sqlite3.connect('message.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, message FROM messages ORDER BY id')
    messages = []
    for row in cursor:
        messages.append(row[1])
    connection.close()
    print(messages)
    return messages

@app.route('/api/messages', methods=['GET'])
def getMessages():
    verify()
    messages = readMessages()
    return jsonify( { 'messages': messages } )

@app.route('/api/messages', methods=['POST'])
def addMessage():
    verify()
    connection = sqlite3.connect('message.db')
    msg = request.form.get('message')
    msg = (msg,)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES(?)", msg)
    connection.commit()
    connection.close()
    messages = readMessages()
    return jsonify( { 'messages': messages } )

app.run(host='0.0.0.0', port=8080)