from decouple import config
from telegram.ext import Updater, CommandHandler

updater = Updater(config('telegram-token'), use_context=True)