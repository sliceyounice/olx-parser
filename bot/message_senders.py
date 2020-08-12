from helpers import create_offer_message
from bot import updater
from mongo import users
import parser_functions
import pytz
import datetime


def send_new_offers():
    offers = parser_functions.find_new_offers()
    if offers:
        messages = [create_offer_message(offer) for offer in offers]
        users_list = users.find_all()
        if users_list:
            date = datetime.datetime.now(pytz.timezone('Europe/Moscow')).strftime("%d/%m/%Y %H:%M:%S")
            [updater.bot.send_message(user['chatId'], f'Новые квартиры на {date}') for user in users_list]
            [updater.bot.send_message(user['chatId'], message) for user in users_list for message in messages]
