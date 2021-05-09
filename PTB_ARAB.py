import random
from telegram import *
from telegram.ext import *
from collections import defaultdict
from functools import wraps
# from time import sleep
PTB_ARAB = map(chr, range(1))
users = defaultdict(dict)
list_user_1 = []
KEYBOARD_1 = ReplyKeyboardMarkup([['Mencari'], ['Kembali Halaman Awal']], resize_keyboard=True, one_time_keyboard=True)
KEYBOARD_2 = ReplyKeyboardMarkup([['Berhenti']], resize_keyboard=True, one_time_keyboard=True)

def scan(current):
    for key, value in users.items():
        if key != current and value.get('status') == 'free':
            return key
    return None

def connect(user, interlocutor):
    users[user]['status'] = 'busy'
    users[user]['interlocutor'] = interlocutor
    users[interlocutor]['status'] = 'busy'
    users[interlocutor]['interlocutor'] = user

def arab_find(update: Update, context: CallbackContext) -> None:
    context.bot.delete_message(update.effective_chat.id, message_id=update.message.message_id)
    user = update.effective_chat.id
    context.bot.send_message(user, 'Mencari...', reply_markup=KEYBOARD_2)
    interlocutor = users[user].get('interlocutor')
    if interlocutor:
        context.bot.send_message(interlocutor, 'Telah berhenti', reply_markup=KEYBOARD_1)
        users[interlocutor]['interlocutor'] = None
        users[user]['interlocutor'] = None
    interlocutor = scan(user)
    if interlocutor:
        connect(user, interlocutor)
        context.bot.send_message(user, 'Sukses Konek {}'.format(interlocutor))
        context.bot.send_message(interlocutor, text='Sukses Konek {}'.format(user))
    else:
        users[user]['status'] = 'free'
    return PTB_ARAB

def arab_disconnect(update: Update, context: CallbackContext) -> None:
    user = update.effective_chat.id
    context.bot.send_message(user, 'Telah berhenti', reply_markup=KEYBOARD_1)
    context.bot.delete_message(update.effective_chat.id, message_id=update.message.message_id)
    users[user]['status'] = 'busy'
    interlocutor = users[user].get('interlocutor')
    if interlocutor:
        context.bot.send_message(interlocutor, 'Telah berhenti',  reply_markup=KEYBOARD_1)
        users[interlocutor]['interlocutor'] = None
        users[user]['interlocutor'] = None
    return PTB_ARAB

def send_action(action):
    def decorator(func):
        @wraps(func)
        def command_func(update:Update, context:CallbackContext, *args, **kwargs):
            user = update.effective_chat.id
            interlocutor = users[user].get('interlocutor')
            context.bot.send_chat_action(chat_id=interlocutor, action=action)
            return func(update, context,  *args, **kwargs)
        return command_func
    return decorator

# @send_action(ChatAction.TYPING)
def arab_text(update: Update, context: CallbackContext) -> None:
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        update.message.reply_chat_action(action=ChatAction.TYPING)
        context.bot.send_message(user, 'Kamu harus mencari dulu /find')
    else:
        context.bot.send_chat_action(interlocutor,ChatAction.TYPING)
        context.bot.send_message(interlocutor, update.message.text)
    return PTB_ARAB

@send_action(ChatAction.TYPING)
def arab_sticker(update: Update, context: CallbackContext) -> None:
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        update.message.reply_chat_action(action=ChatAction.TYPING)
        context.bot.send_message(user, 'Kamu harus mencari dulu /find')
    else:
        context.bot.send_sticker(interlocutor, update.message.sticker.file_id)
    return PTB_ARAB

@send_action(ChatAction.RECORD_AUDIO)
@send_action(ChatAction.UPLOAD_AUDIO)
def arab_voice(update: Update, context: CallbackContext) -> None:
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        context.bot.send_message(user, text='Kamu harus mencari dulu /find')
    else:
        context.bot.send_voice(interlocutor, update.message.voice.file_id)
    return PTB_ARAB

def arab_photo(update: Update, context: CallbackContext):
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        context.bot.send_message(user, text='Kamu harus mencari dulu /find')
    else:
        context.bot.send_photo(interlocutor, update.message.photo[-1].file_id)
    return PTB_ARAB

def arab_video(update: Update, context: CallbackContext):
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        context.bot.send_message(user, text='Kamu harus mencari dulu /find')
    else:
        context.bot.send_video(interlocutor, update.message.video.file_id)
    return PTB_ARAB

def arab_video_note(update: Update, context: CallbackContext):
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        context.bot.send_message(user, text='Kamu harus mencari dulu /find')
    else:
        context.bot.send_video_note(interlocutor, update.message.video_note.file_id)
    return PTB_ARAB

def arab_invoice(update: Update, context: CallbackContext):
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        context.bot.send_message(user, text='Kamu harus mencari dulu /find')
    else:
        context.bot.send_invoice(interlocutor, update.message.invoice)
    return PTB_ARAB

# PTB_ARAB:[
#                     MessageHandler(Filters.command | Filters.regex('Mencari'), arab_find),
#                     MessageHandler(Filters.command | Filters.regex('Berhenti'), arab_disconnect),
#                     MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
#                     MessageHandler(Filters.text, arab_text),
#                     MessageHandler(Filters.sticker, arab_sticker),
#                     MessageHandler(Filters.voice, arab_voice),
#                     MessageHandler(Filters.photo, arab_photo),
#                     MessageHandler(Filters.video, arab_video),
#                     MessageHandler(Filters.video_note, arab_video_note),
#                     MessageHandler(Filters.invoice, arab_invoice)]