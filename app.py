from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)


@app.route("/get", methods=['GET'])
def get_call():
    return "Hello from GET call"


@app.route("/post", methods=['POST'])
def post_call():
    data = request.json
    headers = request.headers
    print(f"data: {data}")
    print(f"headers: {headers.get('Key')}")
    return "Hello from POST call"


@app.route("/token", methods=['GET'])
def token():
    return str(uuid4())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
