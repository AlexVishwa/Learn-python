from datetime import datetime,date

# datetimenow = datetime.now()
# print(datetimenow)                      # 2021-07-08 07:34:46.549883
# day = datetimenow.day                   # 8
# month = datetimenow.month               # 7
# year = datetimenow.year                 # 2021
# hour = datetimenow.hour                 # 7
# minute = datetimenow.minute             # 38
# second = datetimenow.second
# timestamp = datetimenow.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# new_year = datetime(2020, 1, 1)
# print(new_year)      # 2020-01-01 00:00:00
# day = new_year.day
# month = new_year.month
# year = new_year.year
# hour = new_year.hour
# minute = new_year.minute
# second = new_year.second
# print(day, month, year, hour, minute) #1 1 2020 0 0
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

#? STRFTIME
# # current date and time
# now = datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t)
# time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# # mm/dd/YY H:M:S format
# print("time one:", time_one)
# time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# # dd/mm/YY H:M:S format
# print("time two:", time_two)

#* STRPTIME

now=datetime.now()
# print(now)
# day=now.day
# month=now.month
# second=now.second
# year=now.year
# hour=now.hour
# minute=now.minute
# timestamp=now.timestamp()
# print('timestamp:',timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}:{second}')
# # %m/%d/%Y, %H:%M:%S
# date_object='December/5/2019, 20:25:10'
# date_string=now.strftime('%B/%d/%Y, %H:%M:%S')
# print(date_string)

date_string='5 December, 2019'
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
time_two = date_object.strftime("%d/%m/%Y, %H:%M:%S")
print(time_two)

# t1=date(year="2025",month="3",day="25")
# t2=date(year="2026",month="1",day="1")
# print(t2-t1)
# TypeError: 'str' object cannot be interpreted as an integer
t1=date(year=2025,month=3,day=25)
t2=date(year=2026,month=1,day=1)
# print(t2-t1)
t3=date(year=1970,month=1,day=1)
print(t3-t1)

# TypeError: __main__.unpacking_country_info() argument after ** must be a mapping, not list