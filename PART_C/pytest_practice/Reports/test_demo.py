import pytest

def test_add():
    assert 10+5 == 15
@pytest.mark.skip(reason="skip")
def test_sub():
    assert 10-5 == 10
def test_login():
    print("Login is executing....")
@pytest.mark.xfail
def test_add_to_cart():
    print("Add cart is executing....")
def test_logout():
    print("Logout is executing....")
def test_extra():
    print("Extra is executing....")