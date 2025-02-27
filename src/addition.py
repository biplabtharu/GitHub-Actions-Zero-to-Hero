# app.py
# This is a test commit
def add(c, d):
    return c + d

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(5,6) == 11
