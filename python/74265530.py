import datetime

import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None
import os

import pickle


def save_obj(obj, name):
    os.mkdir(f'obj') if not os.path.exists('obj') else None

    with open(f'obj/{name}.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    try:
        with open(f'obj/{name}.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None


today_df = pd.DataFrame(columns=['id', 'date', 'count'])
today_file_name = datetime.datetime.now().strftime("%Y%m%d")
save_obj(today_df, today_file_name)

yesterday_df = pd.DataFrame(columns=['id', 'date', 'count'])
yesterday_file_name = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")
load_obj(yesterday_file_name)


def is_dataFrames_equal(today_df, yesterday_df):
    if (len(yesterday_df) == len(today_df)):
        # len(yesterday_df) == len(today_df) and there is no changes
        if (today_df['id'] == yesterday_df['id']).all() and (today_df['date'] == yesterday_df['date']).all() and (
                today_df['count'] == yesterday_df['count']).all():
            return True
        # len(yesterday_df) == len(today_df) and there is changes
        else:
            return False
    # len(yesterday_df) != len(today_df)
    else:
        return False


if is_dataFrames_equal(today_df, yesterday_df):
    print('no new data found.')
    exit()

# today_df - yesterday_df
diff_df = today_df[~today_df.isin(yesterday_df).all(1)]

df = today_df.copy(deep=True)
