from cdc import parse_number


def test_parse_complex_number():
    assert parse_number("3+j4") == 3+4j


def test_parse_real_number():
    assert parse_number("5") == 5
