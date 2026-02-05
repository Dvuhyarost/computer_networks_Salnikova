@echo off
chcp 65001 >nul
for %%s in (google.com yandex.ru github.com youtube.com wikipedia.org mail.ru vk.com twitch.tv reddit.com stackoverflow.com) do (
    ping %%s > "%%s.txt"
)
python 1.py
del *.txt