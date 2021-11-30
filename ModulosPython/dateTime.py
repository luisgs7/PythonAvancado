from datetime import datetime

d1 = datetime.strptime('20/04/1990 20:00:30', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('22/04/1990 20:00:50', '%d/%m/%Y %H:%M:%S')

print(d2.second)
print(d2 < d1)
print(d1 < d2)
print(d1.timestamp())

d3 = datetime.fromtimestamp(640652430.0)
print(d3)
print(d3.day)
print(d3.second)
print(d3.microsecond)
