from datatime import datetime
from pytz import timezon
format = "%H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC')
print(now_utc.strftime(format))

