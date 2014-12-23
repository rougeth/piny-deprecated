from src.shortener import Base62


def test_base62_to_decimal():
    n = Base62()
    assert n.to_decinal('abc') == '39134'


def test_base62_from_decimal():
    n = Base62()
    assert n.from_decinal('39134') == 'abc'
