# app.py
# This is a test commit
def add(e, f):
    return e + f

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(5,6) == 11
    assert add(10,11) == 21
