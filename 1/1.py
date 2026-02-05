import re
import csv

sites = ["google.com", "yandex.ru", "github.com", "youtube.com", "wikipedia.org",
         "mail.ru", "vk.com", "twitch.tv", "reddit.com", "stackoverflow.com"]

with open("ping.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Site", "Min", "Max", "Avg"])
    for site in sites:
        try:
            txt = open(site + ".txt", encoding="cp866").read()
            min_, max_, avg_ = re.search(r"Minimum\D+(\d+).*Maximum\D+(\d+).*Average\D+(\d+)", txt).groups()
            w.writerow([site, min_, max_, avg_])
        except:
            w.writerow([site, "err", "err", "err"])
