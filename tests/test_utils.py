from src.utils import *

def test_add():
    assert add(3,4) == 7    


def test_regression_get_grid_info(data_regression):
    info = get_grid_info()
    data_regression.check(info)