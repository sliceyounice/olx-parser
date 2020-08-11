import os
from telegram.ext import Updater, CommandHandler

updater = Updater(token=os.environ['telegram-token'], use_context=True)