import datetime, pytz

date = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d/%m/%Y %H:%M:%S")
print(date)