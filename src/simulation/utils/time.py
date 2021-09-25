from datetime import datetime


def get_current_timestring():
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
    return dt_string
