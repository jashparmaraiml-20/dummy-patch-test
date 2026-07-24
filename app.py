from flask import Flask, request, make_response
import secrets
app = Flask(__name__)

@app.route("/data")
def data():
    origin = request.headers.get("Origin")
    resp = make_response("sensitive_data")
    if origin == "https://example.com":
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Access-Control-Allow-Credentials"] = "true"
    session_token = secrets.token_urlsafe(32)
    resp.set_cookie("session_id", session_token, httponly=True, secure=True, samesite="Lax")
    return resp

if __name__ == "__main__":
    app.run(port=5000)
