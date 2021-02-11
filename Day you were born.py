from datetime import datetime
y, m, d = map(int, input().split())
birthday = datetime(y, m, d)
print("You were born on ", end='')
if birthday.weekday() == 0:
  print("Monday")
elif birthday.weekday() == 1:
  print("Tuesday")
elif birthday.weekday() == 2:
  print("Wednesday")
elif birthday.weekday() == 3:
  print("Thursday")
elif birthday.weekday() == 4:
  print("Friday")
elif birthday.weekday() == 5:
  print("Saturday")
elif birthday.weekday() == 6:
  print("Sunday")