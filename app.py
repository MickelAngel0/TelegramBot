#Version - 0.1

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, CallbackQueryHandler
from telegram import ChatAction, ParseMode
from telegram.error import TelegramError
import os, re

TOKEN = '1058006375:AAGSy5cTdE5Fn0iYB_FxtE8kes_HQsPIDGw'
Channels = ['@FGTest1', -1001419460071]

PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def Start(update, context):
    print('Start Function')
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="STart Button")


def Main(update, context):
    print('Main Function')
    if update.message.text:
        Text(update, context)
    elif update.message.sticker:
        Sticker(update, context)
    elif update.message.photo:
        Photo(update, context)
    elif update.message.video:
        Video(update, context)
    elif update.message.document:
        Document(update, context)
    elif update.message.audio:
        Audio(update, context)


def Command(update, context):
    print('Commmad Function')
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Command Function")


def CallBack(update, context):
    print('CallBack Function')
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="CallBack Function")


def Text(update, context):
    print("Message Is Text")
    for i in Channels:
        try:
            updater.bot.sendMessage(chat_id=i,
                                    text=update.message.text_html,
                                    parse_mode=ParseMode.HTML)
        except TelegramError:
            print("TelegramError")
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Text Message Published Successfully")


def Photo(update, context):
    print("Message Contains Photo")
    for i in Channels:
        try:
            updater.bot.sendPhoto(chat_id=i,
                                  photo=update.message.photo[-1],
                                  caption=update.message.caption_html,
                                  parse_mode=ParseMode.HTML)
        except TelegramError:
            print("TelegramError")
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Photo Published Successfully")


def Video(update, context):
    print("Message Contains Video")
    for i in Channels:
        try:
            updater.bot.sendVideo(chat_id=i,
                                  video=update.message.video,
                                  caption=update.message.caption_html,
                                  parse_mode=ParseMode.HTML)
        except TelegramError:
            print("TelegramError")
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Video File Published Successfully")


def Document(update, context):
    print("Message Contains Document")
    for i in Channels:
        try:
            updater.bot.sendDocument(chat_id=i,
                                     document=update.message.document.file_id,
                                     caption=update.message.caption_html,
                                     parse_mode=ParseMode.HTML)
        except TelegramError:
            print("TelegramError")
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Document File Published Successfully")


def Audio(update, context):
    print("Message Contains Audio")
    for i in Channels:
        try:
            updater.bot.sendAudio(chat_id=i,
                                  audio=update.message.audio,
                                  caption=update.message.caption_html,
                                  parse_mode=ParseMode.HTML)
        except TelegramError:
            print("TelegramError")
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Audio File Published Successfully")


def Sticker(update, context):
    print("Message is Sticker")
    for i in Channels:
        try:
            updater.bot.sendSticker(chat_id=i,
                                    sticker=update.message.sticker)
        except TelegramError:
            print("TelegramError")
    updater.bot.sendChatAction(chat_id=update.message.chat_id,
                               action=ChatAction.TYPING)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                            text="Sticker Published Successfully")


dispatcher.add_handler(CallbackQueryHandler(CallBack))
dispatcher.add_handler(CommandHandler('start', Start))
dispatcher.add_handler(MessageHandler(Filters.command, Command))
dispatcher.add_handler(MessageHandler(Filters.all, Main))


updater.start_polling()
'''
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook('https:// <site> /' + TOKEN)
'''
updater.idle()
