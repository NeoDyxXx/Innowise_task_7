import pandas as pd
import os
import time

DIRECTORY_OF_LOGS = os.getenv('DIRECTORY_OF_LOGS', '/home/ndx/Innowise tasks/Innowise_task_7/logs')
SPLIT_SIZE = int(os.getenv('SPLIT_SIZE', '10000'))

def main():
    data = pd.read_csv('./data.csv')
    list_of_dataframes = []

    count = 0
    for i in range(SPLIT_SIZE, data.shape[0], SPLIT_SIZE):
        list_of_dataframes.append(data.iloc[i-SPLIT_SIZE:i])
        count += 1

    list_of_dataframes.append(data.iloc[SPLIT_SIZE * count:])

    os.chdir(DIRECTORY_OF_LOGS)
    print(os.listdir())
    if os.listdir().__len__() == 0:
        count = 0
    else:
        count = max([int(i.split('.')[0].replace('log_', '')) for i in os.listdir()]) + 1

    for dataframe in list_of_dataframes:
        dataframe.to_csv(os.path.join(DIRECTORY_OF_LOGS, 'log_' + str(count) + '.csv'), index=False)
        print('log_' + str(count) + '.csv created.', flush=True)
        count += 1
        time.sleep(5)

if __name__ == "__main__":
    main()