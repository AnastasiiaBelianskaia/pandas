import pandas as pd


def drop_na():
    """ Removes rows with empty cells.
    Doesn't change the original Data Frame.
    To change the original df use dropna(inplace = True)"""

    df = pd.read_csv('bad_data.csv')
    new_df = df.dropna()
    return new_df.to_string()


def fill_na():
    """ Replaces empty cells with a new value.
    Doesn't change the original Data Frame.
    To change the original df use fillna(inplace = True)"""

    df = pd.read_csv('bad_data.csv')
    new_df = df.fillna(111111)
    return new_df.to_string()


def replace_for_specified_column():
    """ Replaces empty cells in specified column with a new value.
        Doesn't change the original Data Frame.
        To change the original df use fillna(inplace = True)"""

    df = pd.read_csv('bad_data.csv')
    new_df = df["Calories"].fillna(222222)
    return new_df.to_string()


def replace_with_mean():
    """ Replaces empty cells with the mean value
    (the sum of all values divided by number of values)."""

    df = pd.read_csv('bad_data.csv')
    mean_val = df['Calories'].mean()
    print('mean_val', mean_val)
    new_df = df['Calories'].fillna(mean_val)
    return new_df


def replace_with_median():
    """ Replaces empty cells with the median value
    (the value in the middle, after you have sorted all values ascending). """

    df = pd.read_csv('bad_data.csv')
    median_val = df['Calories'].median()
    print('median_val', median_val)
    new_df = df['Calories'].fillna(median_val)
    return new_df


def replace_with_mode():
    """ Replaces empty cells with the mode value
     (the value that appears most frequently.)."""

    df = pd.read_csv('bad_data.csv')
    mode_val = df['Calories'].mode()[0]
    print('mode_val', mode_val)
    new_df = df['Calories'].fillna(mode_val)
    return new_df


def wrong_date():
    df = pd.read_csv('bad_data_format.csv')
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    return df.to_string()


def wrong_data():
    """ For small data sets use df.loc[row_num, 'row_name'] = new_value."""

    # Wrong duration in row 7
    df = pd.read_csv('bad_data_wrong_val.csv')
    for x in df.index:
        if df.loc[x, "Duration"] > 120:
            df.loc[x, "Duration"] = 120
    # Or drop it:
    # for x in df.index:
    #     if df.loc[x, "Duration"] > 120:
    #         df.drop(x, inplace=True)
    return df


def duplicates():
    """ Use .drop_duplicates(inplace=True) to remove from the original DataFrame"""

    df = pd.read_csv('bad_data_duplicates.csv')
    print(df.duplicated())
    new_df = df.drop_duplicates()
    return new_df


if __name__ == '__main__':
    print(drop_na())
    print('----------')
    print(fill_na())
    print('----------')
    print(replace_for_specified_column())
    print('----------')
    print(replace_with_mean())
    print('----------')
    print(replace_with_median())
    print('----------')
    print(replace_with_mode())
    print('----------')
    print(wrong_date())
    print('----------')
    print(wrong_data())
    print('----------')
    print(duplicates())
