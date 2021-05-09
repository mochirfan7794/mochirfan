from telegram import *
from telegram.ext import *
from time import sleep
from PTB_BTNS import *
from PTB_KANJI import *
from PTB_HIRAGANA import *
from PTB_KATAKANA import *
from PTB_MALAYSIA import *
from PTB_INGGRIS import *
from PTB_ARAB import *
from PTB_KOREA import *
from PTB_JERMAN import *
from PTB_RUSIA import *
from PTB_BELANDA import *
from PTB_CHINA import *
from PTB_THAILAND import *
from PTB_MYANMAR import *
from PTB_INDIA import *

from PTB_JAWA import *
from PTB_SUNDA import *
from PTB_MADURA import *
from PTB_BETAWI import *
from PTB_BUGIS import *
from PTB_MINANGKABAU import *
from PTB_BANJAR import *
from PTB_ACEH import *
from PTB_BALI import *
from PTB_PALEMBANG import *



CYMAP = map(chr, range(1))

# KEYBOARD_1 = ReplyKeyboardMarkup([['Mencari'], ['Kembali Halaman Awal']], resize_keyboard=True, one_time_keyboard=True)
# KEYBOARD_2 = ReplyKeyboardMarkup([['Berhenti']], resize_keyboard=True, one_time_keyboard=True)

PHOTO = 'https://drive.google.com/file/d/1Up6HHFXeiqcz_tI5qTsp7u_FzIY3wcSc/view?usp=sharing'

def start(update:Update, context:CallbackContext):
    text_1 = 'Welcome '
    inline_keyboard = InlineKeyboardMarkup(buttons_start)
    MyChannel = context.bot.get_chat_member('@cyber_malindo_project', update.effective_user.id)
    if MyChannel.status == 'left' or MyChannel.status == 'kicked':
        update.message.reply_text('Silahkan join', reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text='Join sini', url='https://t.me/cyber_malindo_project')]]))
    elif context.user_data.get(SWIPE_1):
        if MyChannel.status == 'left' or MyChannel.status == 'kicked':
            update.callback_query.answer()
            update.callback_query.edit_message_text('Ma', reply_markup=inline_keyboard)
        else:
            update.callback_query.answer()
            update.callback_query.edit_message_text('Mo', reply_markup=inline_keyboard)
    else:
        # update.message.bot.delete_message(update.effective_chat.id, update.message.message_id)
        update.message.reply_text('Silahkan klik tombol pilihan berikut untuk melanjutkan.', reply_markup=inline_keyboard)
    context.user_data[SWIPE_1] = False
    return CYMAP

# MASUK KE BOT
def masuk_ke_bot(update:Update, context:CallbackContext):
    text_2 = 'Silahkan klik tombol pilihan berikut untuk melanjutkan.'
    text_command = 'Perintah [*Kembali*](http://t.me/Pesawat_Kertas_Bot) sedang diproses\.'
    MyChannel = context.bot.get_chat_member('@cyber_malindo_project', update.effective_user.id)
    inline_keyboard = InlineKeyboardMarkup(buttons_kebot)
    if context.user_data.get(DUKUNGAN):
        if MyChannel.status == 'left' or MyChannel.status == 'kicked':
            update.callback_query.edit_message_text('Bacot', reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text='Klik disini', url='https://t.me/cyber_malindo_project')]]))
        else:
            update.callback_query.answer()
            update.callback_query.message.reply_text(text_2, reply_markup=inline_keyboard)
    elif context.user_data.get(MASUK_KE_BOT_BACK):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text_2, reply_markup=inline_keyboard)
    else:
        if MyChannel.status == 'left' or MyChannel.status == 'kicked':
            context.bot.delete_message(update.effective_chat.id, update.message.message_id)
            update.message.reply_text(text_command, reply_markup=ReplyKeyboardRemove(), parse_mode=ParseMode.MARKDOWN_V2)
            sleep(5)
            update.message.reply_text('Silahkan Join', reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text='Klik disini', url='https://t.me/cyber_malindo_project')]]))
        else:
            context.bot.delete_message(update.effective_chat.id, update.message.message_id)
            update.message.reply_text(text_command, reply_markup=ReplyKeyboardRemove(), parse_mode=ParseMode.MARKDOWN_V2)
            sleep(5)
            update.message.reply_text(text_2, reply_markup=inline_keyboard)
    context.user_data[DUKUNGAN] = False
    context.user_data[MASUK_KE_BOT_BACK] = False
    return CYMAP

def rekoba(update:Update, context:CallbackContext):
    text_2 = 'Silahkan klik tombol pilihan berikut untuk melanjutkan.'
    buttons_1 = [[InlineKeyboardButton('Bahasa Asing', callback_data=str(ASING)),
                  InlineKeyboardButton('Bahasa Lokal', callback_data=str(LOKAL))],
                 [InlineKeyboardButton('Kembali', callback_data=str(MASUK_KE_BOT_BACK))]]
    inline_keyboard = InlineKeyboardMarkup(buttons_1)
    if context.user_data.get(REKOBA):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text_2, reply_markup=inline_keyboard)
    elif context.user_data.get(REPETI):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text_2, reply_markup=inline_keyboard)
    elif context.user_data.get(REUNI):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text=text_2, reply_markup=inline_keyboard)
    context.user_data[REKOBA] = False
    context.user_data[REPETI] = False
    context.user_data[REUNI] = False
    return CYMAP

def bahasa(update:Update, context:CallbackContext):
    text_1 = 'nkjscksjckjnck......'
    inline_keyboard_asing = InlineKeyboardMarkup(buttons_asing)
    inline_keyboard_lokal = InlineKeyboardMarkup(buttons_lokal)
    if context.user_data.get(ASING):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text_1,reply_markup=inline_keyboard_asing)
    elif context.user_data.get(LOKAL):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text_1,reply_markup=inline_keyboard_lokal)
    context.user_data[ASING] = False
    context.user_data[LOKAL] = False
    return CYMAP

def jepang(update:Update, context:CallbackContext):
    text_1 = 'pilih salah satu'
    inline_keyboard_jepang = InlineKeyboardMarkup(buttons_jepang)
    if context.user_data.get(JEPANG):
        update.callback_query.answer()
        update.callback_query.edit_message_text(text_1,reply_markup=inline_keyboard_jepang)
    context.user_data[JEPANG] = False
    return CYMAP

def buttons_kanji(update: Update, context: CallbackContext):
    text_1 = 'Kanji'
    chat_id = update.effective_chat.id
    if context.user_data.get(KANJI):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[KANJI] = False
    return PTB_KANJI
def jepang_kanji(update:Update, context:CallbackContext):
    context.user_data[KANJI] = True
    buttons_kanji(update, context)
    return PTB_KANJI

def buttons_hiragana(update: Update, context: CallbackContext):
    text_1 = 'Hiragana'
    chat_id = update.effective_chat.id
    if context.user_data.get(HIRAGANA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[KANJI] = False
    return PTB_HIRAGANA
def jepang_hiragana(update:Update, context:CallbackContext):
    context.user_data[HIRAGANA] = True
    buttons_hiragana(update, context)
    return PTB_HIRAGANA

def buttons_katakana(update: Update, context: CallbackContext):
    text_1 = 'Katagana'
    chat_id = update.effective_chat.id
    if context.user_data.get(KATAKANA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[KATAKANA] = False
    return PTB_KATAKANA
def jepang_katakana(update:Update, context:CallbackContext):
    context.user_data[KATAKANA] = True
    buttons_katakana(update, context)
    return PTB_KATAKANA

def buttons_malaysia(update: Update, context: CallbackContext):
    text_1 = 'Malaysia'
    chat_id = update.effective_chat.id
    if context.user_data.get(MALAYSIA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[MALAYSIA] = False
    return PTB_MALAYSIA
def malaysia(update:Update, context:CallbackContext):
    context.user_data[MALAYSIA] = True
    buttons_malaysia(update, context)
    return PTB_MALAYSIA

def buttons_inggris(update: Update, context: CallbackContext):
    text_1 = ("Bahasa *Inggris* adalah bahasa Indo\-Eropa dalam kelompok bahasa Jermanik Barat\. " 
              "Bahasa Inggris modern secara luas dianggap sebagai lingua franca dunia dan merupakan bahasa standar di berbagai bidang, " 
              "termasuk pengkodean komputer, bisnis internasional, dan pendidikan tinggi\. ")
    chat_id = update.effective_chat.id
    if context.user_data.get(INGGRIS):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, parse_mode=ParseMode.MARKDOWN_V2, reply_markup=KEYBOARD_1)
    context.user_data[INGGRIS] = False
    return PTB_INGGRIS
def inggris(update:Update, context:CallbackContext):
    context.user_data[INGGRIS] = True
    buttons_inggris(update, context)
    return PTB_INGGRIS

def buttons_arab(update: Update, context: CallbackContext):
    text_1 = 'Arab'
    chat_id = update.effective_chat.id
    if context.user_data.get(ARAB):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[ARAB] = False
    return PTB_ARAB
def arab(update:Update, context:CallbackContext):
    context.user_data[ARAB] = True
    buttons_arab(update, context)
    return PTB_ARAB

def buttons_korea(update: Update, context: CallbackContext):
    text_1 = 'Korea'
    chat_id = update.effective_chat.id
    if context.user_data.get(KOREA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[KOREA] = False
    return PTB_KOREA
def korea(update:Update, context:CallbackContext):
    context.user_data[KOREA] = True
    buttons_korea(update, context)
    return PTB_KOREA

def buttons_jerman(update: Update, context: CallbackContext):
    text_1 = 'Jerman'
    chat_id = update.effective_chat.id
    if context.user_data.get(JERMAN):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[JERMAN] = False
    return PTB_JERMAN
def jerman(update:Update, context:CallbackContext):
    context.user_data[JERMAN] = True
    buttons_jerman(update, context)
    return PTB_JERMAN

def buttons_rusia(update: Update, context: CallbackContext):
    text_1 = 'Rusia'
    chat_id = update.effective_chat.id
    if context.user_data.get(RUSIA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[RUSIA] = False
    return PTB_RUSIA
def rusia(update:Update, context:CallbackContext):
    context.user_data[RUSIA] = True
    buttons_rusia(update, context)
    return PTB_RUSIA

def buttons_belanda(update: Update, context: CallbackContext):
    text_1 = 'Belanda'
    chat_id = update.effective_chat.id
    if context.user_data.get(BELANDA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[BELANDA] = False
    return PTB_BELANDA
def belanda(update:Update, context:CallbackContext):
    context.user_data[BELANDA] = True
    buttons_belanda(update, context)
    return PTB_BELANDA

def buttons_china(update: Update, context: CallbackContext):
    text_1 = 'China'
    chat_id = update.effective_chat.id
    if context.user_data.get(CHINA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[CHINA] = False
    return PTB_CHINA
def china(update:Update, context:CallbackContext):
    context.user_data[CHINA] = True
    buttons_china(update, context)
    return PTB_CHINA

def buttons_thailand(update: Update, context: CallbackContext):
    text_1 = 'Thailand'
    chat_id = update.effective_chat.id
    if context.user_data.get(THAILAND):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[THAILAND] = False
    return PTB_THAILAND
def thailand(update:Update, context:CallbackContext):
    context.user_data[THAILAND] = True
    buttons_thailand(update, context)
    return PTB_THAILAND

def buttons_myanmar(update: Update, context: CallbackContext):
    text_1 = 'Myanmar'
    chat_id = update.effective_chat.id
    if context.user_data.get(MYANMAR):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[MYANMAR] = False
    return PTB_MYANMAR
def myanmar(update:Update, context:CallbackContext):
    context.user_data[MYANMAR] = True
    buttons_myanmar(update, context)
    return PTB_MYANMAR

def buttons_india(update: Update, context: CallbackContext):
    text_1 = 'India'
    chat_id = update.effective_chat.id
    if context.user_data.get(INDIA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[INDIA] = False
    return PTB_INDIA
def india(update:Update, context:CallbackContext):
    context.user_data[INDIA] = True
    buttons_india(update, context)
    return PTB_INDIA

def buttons_jawa(update: Update, context: CallbackContext):
    text_1 = 'Jawa'
    chat_id = update.effective_chat.id
    if context.user_data.get(JAWA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[JAWA] = False
    return PTB_JAWA
def jawa(update:Update, context:CallbackContext):
    context.user_data[JAWA] = True
    buttons_jawa(update, context)
    return PTB_JAWA

def buttons_sunda(update: Update, context: CallbackContext):
    text_1 = 'Sunda'
    chat_id = update.effective_chat.id
    if context.user_data.get(SUNDA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[SUNDA] = False
    return PTB_SUNDA
def sunda(update:Update, context:CallbackContext):
    context.user_data[SUNDA] = True
    buttons_sunda(update, context)
    return PTB_SUNDA

def buttons_madura(update: Update, context: CallbackContext):
    text_1 = 'Madura'
    chat_id = update.effective_chat.id
    if context.user_data.get(MADURA):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[MADURA] = False
    return PTB_MADURA
def madura(update:Update, context:CallbackContext):
    context.user_data[MADURA] = True
    buttons_madura(update, context)
    return PTB_MADURA

def buttons_betawi(update: Update, context: CallbackContext):
    text_1 = 'Betawi'
    chat_id = update.effective_chat.id
    if context.user_data.get(BETAWI):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[BETAWI] = False
    return PTB_BETAWI
def betawi(update:Update, context:CallbackContext):
    context.user_data[BETAWI] = True
    buttons_betawi(update, context)
    return PTB_BETAWI

def buttons_bugis(update: Update, context: CallbackContext):
    text_1 = 'Bugis'
    chat_id = update.effective_chat.id
    if context.user_data.get(BUGIS):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[BUGIS] = False
    return PTB_BUGIS
def bugis(update:Update, context:CallbackContext):
    context.user_data[BUGIS] = True
    buttons_bugis(update, context)
    return PTB_BUGIS

def buttons_minangkabau(update: Update, context: CallbackContext):
    text_1 = 'Minangkabau'
    chat_id = update.effective_chat.id
    if context.user_data.get(MINANGKABAU):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[MINANGKABAU] = False
    return PTB_MINANGKABAU
def minangkabau(update:Update, context:CallbackContext):
    context.user_data[MINANGKABAU] = True
    buttons_minangkabau(update, context)
    return PTB_MINANGKABAU

def buttons_banjar(update: Update, context: CallbackContext):
    text_1 = 'Banjar'
    chat_id = update.effective_chat.id
    if context.user_data.get(BANJAR):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[BANJAR] = False
    return PTB_BANJAR
def banjar(update:Update, context:CallbackContext):
    context.user_data[BANJAR] = True
    buttons_banjar(update, context)
    return PTB_BANJAR

def buttons_aceh(update: Update, context: CallbackContext):
    text_1 = 'Aceh'
    chat_id = update.effective_chat.id
    if context.user_data.get(ACEH):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[ACEH] = False
    return PTB_ACEH
def aceh(update:Update, context:CallbackContext):
    context.user_data[ACEH] = True
    buttons_aceh(update, context)
    return PTB_ACEH

def buttons_bali(update: Update, context: CallbackContext):
    text_1 = 'Bali'
    chat_id = update.effective_chat.id
    if context.user_data.get(BALI):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[BALI] = False
    return PTB_BALI
def bali(update:Update, context:CallbackContext):
    context.user_data[BALI] = True
    buttons_bali(update, context)
    return PTB_BALI

def buttons_palembang(update: Update, context: CallbackContext):
    text_1 = 'Palembang'
    chat_id = update.effective_chat.id
    if context.user_data.get(PALEMBANG):
        update.callback_query.answer()
        update.callback_query.bot.sendMessage(chat_id, text_1, reply_markup=KEYBOARD_1)
    context.user_data[PALEMBANG] = False
    return PTB_PALEMBANG
def palembang(update:Update, context:CallbackContext):
    context.user_data[PALEMBANG] = True
    buttons_palembang(update, context)
    return PTB_PALEMBANG



def masuk_ke_bot_go(update:Update, context:CallbackContext):
    context.user_data[DUKUNGAN] = True
    masuk_ke_bot(update, context)
    return CYMAP

def masuk_ke_bot_back(update:Update, context:CallbackContext):
    context.user_data[MASUK_KE_BOT_BACK] = True
    masuk_ke_bot(update, context)
    return CYMAP

def rekoba_go(update:Update, context:CallbackContext):
    context.user_data[REKOBA] = True
    rekoba(update, context)
    return CYMAP

def repeti_go(update:Update, context:CallbackContext):
    context.user_data[REPETI] = True
    rekoba(update, context)
    return CYMAP

def reuni_go(update:Update, context:CallbackContext):
    context.user_data[REUNI] = True
    rekoba(update, context)
    return CYMAP

def asing_go(update:Update, context:CallbackContext):
    context.user_data[ASING] = True
    bahasa(update, context)
    return CYMAP

def jepang_go(update:Update, context:CallbackContext):
    context.user_data[JEPANG] = True
    jepang(update, context)
    return CYMAP

def lokal_go(update:Update, context:CallbackContext):
    context.user_data[LOKAL] = True
    bahasa(update, context)
    return CYMAP