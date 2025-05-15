from bad_practice import get_hardcoded_key

def test_hardcoded_key():
    assert get_hardcoded_key() == "123456-SECRET-API-KEY"
