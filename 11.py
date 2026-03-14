from datetime import datetime, date, timedelta
a = input()
datee = datetime.strptime(a, "%Y-%m-%d").date()
gap = timedelta(days=10)
print(datee + gap)


from datetime import datetime, date, timedelta
a = input()
datee1 = datetime.strptime(a, "%Y-%m-%d").date()
b = input()
datee2 = datetime.strptime(b, "%Y-%m-%d").date()
gap = datee2 - datee1
print(gap.days)


from datetime import datetime

a = input()
d = datetime.strptime(a, "%Y-%m-%d").date()

if d.weekday() >= 5:
    print("Weekend")
else:
    print("Weekday")


