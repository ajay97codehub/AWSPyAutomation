# tests/test_auth.py

from awspyautomation.auth import login

def test_login_success():
    assert login('ajay', 'ajay123') == True

def test_login_failure():
    assert login('ajay', 'wrong_password') == False
