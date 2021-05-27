from app.app import encode, decode

MESSAGE = "This is a test message"
KEY = "This is a test key"
EXPECTED_ENCODING = "wqjDkMOSw6ZAw5LDpkDDgkDDqMOKw6bDqEDDmMOKw6zDh8OJw5DDmA=="


def test_encode():
    result = encode(KEY, MESSAGE)
    assert result == EXPECTED_ENCODING


def test_decode():
    result = decode(KEY, EXPECTED_ENCODING)
    assert result == MESSAGE
