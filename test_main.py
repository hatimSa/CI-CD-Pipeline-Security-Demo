from main import get_api_key
import os
def test_get_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "test123")
    assert get_api_key() == "test123"
