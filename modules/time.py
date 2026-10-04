from datetime import datetime


class TimeModule:
    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")
