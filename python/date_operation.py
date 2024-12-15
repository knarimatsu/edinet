from datetime import datetime, timedelta

today = datetime.now()
yesterday = datetime.today() - timedelta(days=1)
tomorrow = datetime.today() + timedelta(days=1)
day_after_tomorrow = datetime.today() + timedelta(days=2)
three_days_later = datetime.today() + timedelta(days=3)
four_days_later = datetime.today() + timedelta(days=4)
five_days_later = datetime.today() + timedelta(days=5)
six_days_later = datetime.today() + timedelta(days=6)
a_week_later = datetime.today() + timedelta(days=7)
