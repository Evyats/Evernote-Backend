from src.auth import pass_hash


def test_hashing():
    password = "some_password"
    hashed = pass_hash.hash(password)
    print(password, hashed)
    assert pass_hash.verify(password, hashed) is True
    assert pass_hash.verify("wrong_password", hashed) is False