import schedule, datetime, time

def job():
    localtime = time.asctime(time.localtime(time.time()))
    print("Local current time :", localtime)


schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(15)
