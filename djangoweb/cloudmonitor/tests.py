from django.test import TestCase

# Create your tests here.
from datetime import datetime, timedelta, time

t = datetime.now()
delta = timedelta(hours=1)

print(t.__format__('%Y-%m-%d %H:%M'))

print((t + delta).__format__('%Y-%m-%d %H:%M'))

# print(time.strftime('%Y-%m-%d %H:%M', t + delta))

# time.t