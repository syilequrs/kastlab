import datetime

def five_days_nazad():
  print(datetime.date.today()- datetime.timedelta(days=5))

five_days_nazad()

def tday_yestday_tmrw():
    print(f"Today is {datetime.date.today()}\nYestarday was\
 {datetime.date.today()- datetime.timedelta(days=1)}\n\
Tomorrow will be {datetime.date.today() + datetime.timedelta(days=1)}")

tday_yestday_tmrw()

def delete_micsecs():
  def drop_micsecs(dt):
    return dt.replace(microsecond=0)

  now = datetime.datetime.now()
  print(f'Original datetime {now}')

  without_micsecs = drop_micsecs(now)
  print(f'Without microseconds {without_micsecs}')
delete_micsecs()

def seconds_dif(date1_str, date2_str):
  date_format = '%Y-%m-%d'

  date1 = datetime.datetime.strptime(date1_str, date_format)
  date2 = datetime.datetime.strptime(date2_str, date_format)

  difference = date2 - date1

  return difference.total_seconds()

day1 = '2025-02-17'

day2 = '2028-02-28'

print(f'Seconds difference is {seconds_dif(day1, day2)}')