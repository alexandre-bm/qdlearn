from hypothesis import given
from hypothesis.strategies import integers

@given(integers(), integers())
def test_addition_commutative(a,b):
    assert a + b == b + a