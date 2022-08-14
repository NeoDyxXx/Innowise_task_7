import pandas as pd
from sender_alert import AlertSender

class AlertSystem:
    def __init__(self, name_of_file, valid_time = 1, check_with_code_zero = False) -> None:
        self.name_of_file = name_of_file
        self.valid_time = valid_time
        self.check_with_code_zero = check_with_code_zero
        self.__init_dataframe()

        self.data['date'] = pd.to_datetime(self.data['date'], unit='s')
        if self.check_with_code_zero:
            self.data = self.data[(self.data['severity'] == 'Error')]
        else:
            self.data = self.data[(self.data['severity'] == 'Error') & (self.data['error_code'] == 203)]

    def check_on_minutes(self):
        self.data['minute'] = self.data['date'].apply(lambda ts: ts.minute)

        if (self.data.groupby('minute').count()['error_code'] > 10).any():
            AlertSender()('More then 10 times of error alert by one minutes in file ' + self.name_of_file.split('/')[2])
        print('execute minute')

    def check_on_hour(self):
        self.data['hour'] = self.data['date'].apply(lambda ts: ts.hour)
        group_data = (self.data.groupby(['bundle_id', 'hour']).count()['error_code'] > 10).groupby('bundle_id').any()

        if group_data.any():
            AlertSender()('More then 10 times of error alert by one hour in file '\
                + self.name_of_file.split('/')[2] + ' in bundle_id ' + str(group_data.index.to_list()))
        
        print('execute hour')

    def __init_dataframe(self):
        self.data = pd.read_csv(self.name_of_file, names=['error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id', 'sdkv', 'test_mode', 'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv', 'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date'])

        while(True):
            if ((self.data.sort_values('date', ascending=False)['date'].iloc[0] - \
                self.data.sort_values('date')['date'].iloc[0]) / 3600) < self.valid_time:
                    name_of_prev_file = self.name_of_file.split('_')[0] + str(int(self.name_of_file.split('.')[0]\
                        .split('_')[1]) - 1) + '.csv'
                    prev_data = pd.read_csv(name_of_prev_file)
                    self.data = pd.concat([self.data, prev_data], names=['error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id', 'sdkv', 'test_mode', 'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv', 'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date'])
            else:
                break