from mongo import users as users


def start(update, context):
    users.save({'chatId': update.message.chat['id'], 'username': update.message.chat['username']})
    update.message.reply_text("Теперь тебе будут приходить уведомления о квартирах в Донецке")


