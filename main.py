import pandas as pd


def dataframe():
    dataset = {
        'cars': ['BMW', 'Volvo', 'Ford'],
        'passings': [3, 7, 2]
    }
    var = pd.DataFrame(dataset, index=["first", "second", "third"])
    return var


def dataframe_row():
    data = {
        'calories': [121, 640, 234],
        'duration': [34, 80, 45]
    }
    df = pd.DataFrame(data)
    row = df.loc[1]
    return row


def dataframe_rows():
    data = {
        'calories': [121, 640, 234],
        'duration': [34, 80, 45]
    }
    df = pd.DataFrame(data)
    rows = df.loc[[0, 2]]
    return rows


def series():
    a = [1, 7, 10]
    var = pd.Series(a)
    print('This is second number : ', var[1])
    return var


def index():
    a = [1, 7, 10]
    var = pd.Series(a, index=['x', 'y', 'z'])
    print('This is z value : ', var['z'])
    return var


def keyvalue():
    calories = {"day1": 420, "day2": 380, "day3": 390}
    var = pd.Series(calories)
    return var


def keyvalueindex():
    calories = {"day1": 420, "day2": 380, "day3": 390}
    var = pd.Series(calories, index=['day1', 'day2'])
    return var


def csv():
    df = pd.read_csv('data.csv')
    return df.to_string()


def read_json():
    df = pd.read_json('https://www.w3schools.com/python/pandas/data.js')
    return df.to_string()


def dict_as_json():
    data = {
        "Duration": {
            "0": 60,
            "1": 60,
            "2": 60,
            "3": 45,
            "4": 45,
            "5": 60
        },
        "Pulse": {
            "0": 110,
            "1": 117,
            "2": 103,
            "3": 109,
            "4": 117,
            "5": 102
        },
        "Maxpulse": {
            "0": 130,
            "1": 145,
            "2": 135,
            "3": 175,
            "4": 148,
            "5": 127
        },
        "Calories": {
            "0": 409,
            "1": 479,
            "2": 340,
            "3": 282,
            "4": 406,
            "5": 300
        }
    }

    df = pd.DataFrame(data)
    return df


def head():
    """Returns first 10 rows"""

    df = pd.read_csv('data.csv')
    return df.head(10)


def tail():
    """Returns last 10 rows"""

    df = pd.read_csv('data.csv')
    return df.tail()


def info():
    df = pd.read_csv('data.csv')
    return df.info()


if __name__ == '__main__':
    print(dataframe())
    print('---------')
    print(dataframe_row())
    print('---------')
    print(dataframe_rows())
    print('---------')
    print(series())
    print('---------')
    print(index())
    print('---------')
    print(keyvalue())
    print('----------')
    print(keyvalueindex())
    print('----------')
    print(csv())
    print('----------')
    print(pd.options.display.max_rows)
    print('----------')
    print(read_json())
    print('----------')
    print(dict_as_json())
    print('----------')
    print(head())
    print('----------')
    print(tail())
    print('----------')
    print(info())
    print('----------')
