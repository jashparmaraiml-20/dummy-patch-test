from flask import Flask, request, make_response
import secrets
app = Flask(__name__)

def generate_session_id():
    return secrets.token_urlsafe(32)

@app.route("/data")
def data():
    origin = request.headers.get("Origin") if request.headers.get("Origin") == "https://example.com" else None
    resp = make_response("sensitive_data")
    if origin:
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.set_cookie("session_id", generate_session_id(), httponly=True, secure=True, samesite="Lax")
    return resp

if __name__ == "__main__":
    app.run(port=5000)
