from datetime import datetime, timedelta


def next_time_interval(date):
    if type(date) == str:
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
    return date + (datetime.min - date.replace(tzinfo=None)) % timedelta(minutes=5)

