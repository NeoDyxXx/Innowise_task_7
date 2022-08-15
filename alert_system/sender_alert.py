class AlertSender:
    def __call__(self, alert_str: str):
        print(alert_str, flush=True)

        # TODO: maybe what even imaging