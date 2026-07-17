from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/data")
def data():
    origin = request.headers.get("Origin", "*")
    resp = make_response("sensitive_data")
    resp.headers["Access-Control-Allow-Origin"] = origin
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.set_cookie("session_id", "secret123")
    return resp

if __name__ == "__main__":
    app.run(port=5000)
