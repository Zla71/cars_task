from datetime import datetime

@staticmethod
def get_currnet_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time