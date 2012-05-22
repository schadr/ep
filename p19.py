year = 1900
c_weekday = 0
c_day = 1
c_month = 0
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
sunday_count = 0

# 171

while year < 2001:
  if c_weekday % 7 == 6 and c_day == 1 and year > 1900:  
    sunday_count += 1
  days_in_month[1] = 28
  if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
    days_in_month[1] = 29
  if c_day == days_in_month[c_month]:
    c_day = 0
    c_month += 1
    if c_month > 11:
      c_month = 0
      year += 1
  c_day += 1
  c_weekday = (c_weekday + 1) % 7

print(sunday_count)
  
