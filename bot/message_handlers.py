from mongo import users as users

def start(update, context):
    if users.save({'chatId': update.message.chat['id'], 'username': update.message.chat['username']}):
        message = "Теперь тебе будут приходить уведомления о квартирах в Донецке"
    else:
        message = "Ты уже подписан на обновления"
    update.message.reply_text(message)


