import requests
import telebot
from bs4 import BeautifulSoup
from time import sleep
url = "https://kman.kyiv.ua/ua/Rezultati-II-miskoho-etapu-Vseukrainskoho-konkursu-zakhistu-2025-2026"
USER_ID = 1788277612
TELEGMRAM_TOKEN = "8617169245:AAHHfGOA1Wsh4XeKpCLiwrnmbp5jZptK56E"
INTERVAL = 60

bot = telebot.TeleBot(TELEGMRAM_TOKEN)



response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.select("section.mceEditable.content p strong span")
    old_sections = []
    for section in sections:
        old_sections.append(section.text)
else:
    print(f"code exited with response status code : {response.status_code}")

while True:
    

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        sections = soup.select("section.mceEditable.content p strong span")
        cur_sections = []
        for section in sections:
            cur_sections.append(section.text)
    else:
        print(f"code exited with response status code : {response.status_code}")


    if cur_sections != old_sections:
        holder = cur_sections[:]
        for el in old_sections:
            holder.remove(el)
        for new_section in holder:

            msg = f"На сайті опубліковані результати для секції:\n<b>{new_section.upper()}</b>"
            print(msg)
            bot.send_message(USER_ID, msg, parse_mode="HTML")

    

        old_sections = cur_sections[:]
    else:
        print("Изменений нет")
    sleep(INTERVAL)