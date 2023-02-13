import pandas as pd
import os

check_file = os.path.isfile('./data.csv')
if (check_file == False):
    df = pd.DataFrame([], columns=['s_no', 'task','status'], index=None)
    df.to_csv('data.csv', index=False)

df = pd.read_csv('data.csv', index_col=0)
