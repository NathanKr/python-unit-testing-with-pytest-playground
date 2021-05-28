import pandas as pd

def add(num1,num2):
    return num1+num2

def get_some_html()->str:
    html : str = '<!DOCTYPE html>\
        <html lang="en">\
        <head>\
            <meta charset="UTF-8">\
            <meta http-equiv="X-UA-Compatible" content="IE=edge">\
            <meta name="viewport" content="width=device-width, initial-scale=1.0">\
            <title>Document</title>\
        </head>\
        <body>\
            <h1>Hello</h1>\
        </body>\
        </html>'
    return html

def get_some_df()->pd.DataFrame:
    df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                  columns=['col1', 'col2', 'col3' , 'col4'])
    return df

def get_grid_info():
    return {
        "Main Grid": {
            "id": 0,
            "cell_count": 1000,
            "active_cells": 300,
            "properties": [
                {"name": "Temperature", "min": 75, "max": 85},
                {"name": "Porosity", "min": 0.3, "max": 0.4},
            ],
        },
        "Refin1": {
            "id": 1,
            "cell_count": 48,
            "active_cells": 44,
            "properties": [
                {"name": "Temperature", "min": 78, "max": 81},
                {"name": "Porosity", "min": 0.36, "max": 0.39},
            ],
        },
    }