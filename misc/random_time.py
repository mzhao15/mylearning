import random
import datetime

start_date = datetime.date(1900,1,1)
end_date = datetime.date.today()

start = datetime.datetime(1900, 1, 1, 00, 00, 00)
days = end_date - start_date
end = start + datetime.timedelta(days = days.days)

for i in range(10):
    random_date = start + (end - start) * random.random()
    print(random_date)


