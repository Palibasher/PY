from Fun_fun import devision
import pytest

@pytest.mark.parametrize("a, b, expected", [(10, 5, 2),
                                            (10,10,1),
                                            (33,-3,-11)])
def test_devision_good(a, b, expected):
    assert devision(a,b) == expected

@pytest.mark.parametrize("exp_err, divider", [(ZeroDivisionError, 0),
                                              (TypeError, "2")])

def test_error_devision(exp_err, divider):
    with pytest.raises(exp_err):
        devision(10/divider)