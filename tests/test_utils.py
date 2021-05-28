from src.utils import *

def test_add():
    assert add(3,4) == 7    

def test_regression_get_grid_info(data_regression):
    info = get_grid_info()
    data_regression.check(info)

def test_regression_get_some_df(dataframe_regression):
    df = get_some_df()
    # this is working basically on numbers
    dataframe_regression.check(df)    

def test_regression_get_some_html(data_regression):
    table : str = get_some_html()
    data_regression.check(table)