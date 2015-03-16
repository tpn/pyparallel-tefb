from flask import Flask, jsonify, make_response

app = Flask('test')

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

import socket
ipaddr = socket.gethostbyname(socket.gethostname())

@app.route("/json")
def json():
    return jsonify(message='Hello, world!')

@app.route("/plaintext")
def plaintext():
    response = make_response(b'Hello, world!')
    response.content_type = 'text/plain'
    return response

def main():
    app.run(host=ipaddr, port=8080)

if __name__ == '__main__':
    main()
