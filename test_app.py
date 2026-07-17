import pytest
from app import app

def test_cors():
    client = app.test_client()
    resp = client.get("/data", headers={"Origin": "https://evil.com"})
    # Secure CORS configuration should NOT reflect evil.com
    assert resp.headers.get("Access-Control-Allow-Origin") != "https://evil.com"

def test_cookie():
    client = app.test_client()
    resp = client.get("/data")
    cookie_header = resp.headers.get("Set-Cookie", "")
    # Secure cookies should contain HttpOnly and Secure
    assert "HttpOnly" in cookie_header
    assert "Secure" in cookie_header
