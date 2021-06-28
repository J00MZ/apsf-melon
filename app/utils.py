"""Application utility functions."""

from datetime import datetime

def get_todays_date():
    return datetime.today().strftime(f'%Y%m%d')

