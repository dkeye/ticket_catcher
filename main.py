import time

import requests
import telebot

from config import TOKEN, ADMIN_ID

ADDRESS = 'https://poravkino.ru/api/schedule?date=2021-09-03'

bot = telebot.TeleBot(TOKEN)


def get_timetable() -> bool:
    response = requests.get(ADDRESS)
    if response.status_code != 200:
        raise requests.HTTPError
    if response.json():
        return True
    return False


def send_admin(text) -> None:
    bot.send_message(ADMIN_ID, text)


def main():
    while True:
        try:
            if get_timetable():
                send_admin('Пора купить билеты')
                return
        except requests.HTTPError:
            send_admin('Ошибка запроса к сайту')
            return

        time.sleep(5 * 60)


if __name__ == '__main__':
    try:
        send_admin('Начало работы')
        main()
    finally:
        send_admin('Бот выключен')
