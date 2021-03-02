import os
import sqlite3
from flask import Flask, request, jsonify, abort
from jwt.jwks import JWKS
from jwt.jwt import JWT

claims = { 'iss': os.environ['OKTA_ISSUER_URI'], 'aud': 'api://default' }
jwks = JWKS(os.environ['OKTA_ISSUER_URI'] + '/v1/keys')

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
        abort(401, description="Unauthorized")
    token = auth[7:]
    try:
        jwt = JWT(token, claims, 2)
        jwks.verify(jwt)
    except Exception as e:
        abort(403, e)

@app.route('/api/messages', methods=['GET'])
def getMessages():
    verify()

@app.route('/api/messages', methods=['POST'])
def addMessage():
    verify()
    msg = request.form.get('message')
    messages.append(msg)
    return jsonify( { 'messages': messages } )

app.run(host='0.0.0.0', port=8080)