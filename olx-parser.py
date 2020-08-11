from bot import updater, CommandHandler
from bot.message_handlers import start
from bot.message_senders import send_new_offers
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


if __name__ == "__main__":
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_new_offers, CronTrigger.from_crontab('0 */1 * * *'))
    scheduler.start()
    updater.start_polling()
    updater.idle()
