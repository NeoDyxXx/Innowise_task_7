class AlertSender:
    def __call__(self, alert_str: str):
        print(alert_str)

        # TODO: make send to email