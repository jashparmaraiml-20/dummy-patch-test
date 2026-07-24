from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/data")
def data():
    request_origin = request.headers.get("Origin")
    allowed_origin = "https://example.com" if request_origin == "https://example.com" else None

    resp = make_response("sensitive_data")

    if allowed_origin is not None:
        resp.headers["Access-Control-Allow-Origin"] = allowed_origin
        resp.headers["Access-Control-Allow-Credentials"] = "true"
    else:
        resp.headers.pop("Access-Control-Allow-Origin", None)
        resp.headers.pop("Access-Control-Allow-Credentials", None)
    resp.set_cookie("session_id", "secret123", httponly=True, secure=True)
    return resp

if __name__ == "__main__":
    app.run(port=5000)
