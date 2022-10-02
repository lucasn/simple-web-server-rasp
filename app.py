from flask import Flask, request, Response
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/", methods=['POST'])
def hello_world():
    print(f'Temperature: {request.data.decode("ascii")}')
    return Response(status=200)