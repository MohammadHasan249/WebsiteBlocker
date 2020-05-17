import time
from datetime import datetime as dt


path = r"C:\Windows\System32\drivers\etc\hosts"
websites = ["www.facebook.com", "facebook.com"]
redirect_ip = "127.0.0.1"

while True:
    year = dt.now().year
    month = dt.now().month
    day = dt.now().day
    start_time = dt(year, month, day, 17)  # chose 5 pm and 9 pm for convenience
    end_time = dt(year, month, day, 21)  # could be any other hours

    # working hours
    if start_time <= dt.now() <= end_time:
        with open(path, "r+") as file:
            lines = file.read()
            for website in websites:
                if website not in lines:
                    file.write(redirect_ip + " " + website + "\n")

    # free hours
    else:
        with open(path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(10)
