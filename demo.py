import datetime,time
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    time.sleep(1)