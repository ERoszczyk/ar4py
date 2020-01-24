from datetime import datetime, timedelta


def next_time_interval(date):
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
    return date + (datetime.min - date) % timedelta(minutes=5)
