import pandas as pd
import os
import sys

try:
    check_file = os.path.isfile('./data.csv')
    if (check_file == False):
        df = pd.DataFrame([], columns=['s_no', 'task','status'], index=None)
        df.to_csv('data.csv', index=False)

    df = pd.read_csv('data.csv', index_col=0)
except:
    print('Error: Unable to read data.csv file.')
    sys.exit('Error: Unable to read data.csv file.')
