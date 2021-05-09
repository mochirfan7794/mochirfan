from telegram import *
from telegram.ext import *

DUKUNGAN, MASUK_KE_BOT_GO, MASUK_KE_BOT_BACK = map(chr, range(1, 4)) # start
REKOBA, REPETI, REUNI = map(chr, range(4, 7)) # masuk_ke_bot
ASING, LOKAL = map(chr, range(7, 9)) # rekoba
INGGRIS, ARAB, JEPANG, KOREA, JERMAN, RUSIA, BELANDA, CHINA, THAILAND, MYANMAR, MALAYSIA, INDIA = map(chr, range(9, 21))
KANJI, HIRAGANA, KATAKANA = map(chr, range(21, 24))
JAWA, SUNDA, MADURA, BETAWI, BUGIS, MINANGKABAU, BANJAR, ACEH, BALI, PALEMBANG = map(chr, range(24, 34))
SWIPE_1, SWIPE_2, SWIPE_3 = map(chr, range(34, 37)) 


OFFSET = 127462 - ord('A')
def flag(code):
    code = code.upper()
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

# START
buttons_start = [[InlineKeyboardButton('DUKUNGAN', callback_data=str(DUKUNGAN))],
                 [InlineKeyboardButton('MASUK KE BOT', callback_data=str(MASUK_KE_BOT_BACK))]]

# MASUK KE BOT
buttons_kebot = [[InlineKeyboardButton('Relasi Komunikasi Bahasa', callback_data=str(REKOBA))],
                 [InlineKeyboardButton('Relasi Perguruan Tinggi', callback_data=str(REPETI))],
                 [InlineKeyboardButton('Relasi Universal', callback_data=str(REUNI))],
                 [InlineKeyboardButton('DUKUNGAN', callback_data=str(DUKUNGAN))]]

# BAHASA
buttons_asing = [[InlineKeyboardButton('Inggris {}'.format(flag('GB')), callback_data=str(INGGRIS)),                
                  InlineKeyboardButton('Arab {}'.format(flag('SA')), callback_data=str(ARAB)),
                  InlineKeyboardButton('Jepang {}'.format(flag('JP')), callback_data=str(JEPANG))],
                 [InlineKeyboardButton('Korea {}'.format(flag('KR')), callback_data=str(KOREA)),
                  InlineKeyboardButton('Jerman {}'.format(flag('DE')), callback_data=str(JERMAN)),
                  InlineKeyboardButton('Rusia {}'.format(flag('RU')), callback_data=str(RUSIA))],
                 [InlineKeyboardButton('Belanda {}'.format(flag('NL')), callback_data=str(BELANDA)),
                  InlineKeyboardButton('China {}'.format(flag('CN')), callback_data=str(CHINA)),
                  InlineKeyboardButton('Thailand {}'.format(flag('TH')), callback_data=str(THAILAND))],
                 [InlineKeyboardButton('Myanmar {}'.format(flag('MM')), callback_data=str(MYANMAR)),
                  InlineKeyboardButton('Malaysia {}'.format(flag('MY')), callback_data=str(MALAYSIA)),
                  InlineKeyboardButton('India {}'.format(flag('IN')), callback_data=str(INDIA))],
                 [InlineKeyboardButton('Kembali', callback_data=str(REKOBA))]]
buttons_lokal = [[InlineKeyboardButton('Jawa', callback_data=str(JAWA)),
                  InlineKeyboardButton('Sunda', callback_data=str(SUNDA)),
                  InlineKeyboardButton('Madura', callback_data=str(MADURA))],
                 [InlineKeyboardButton('Betawi', callback_data=str(BETAWI)),
                  InlineKeyboardButton('Bugis', callback_data=str(BUGIS)),
                  InlineKeyboardButton('Minangkabau', callback_data=str(MINANGKABAU))],
                 [InlineKeyboardButton('Banjar', callback_data=str(BANJAR)),
                  InlineKeyboardButton('Aceh', callback_data=str(ACEH)),
                  InlineKeyboardButton('Bali', callback_data=str(BALI))],
                 [InlineKeyboardButton('Palembang', callback_data=str(PALEMBANG)),
                  InlineKeyboardButton('Kembali', callback_data=str(REKOBA))]]

buttons_jepang = [[InlineKeyboardButton('Kanji', callback_data=str(KANJI)),
                   InlineKeyboardButton('Hiragana', callback_data=str(HIRAGANA)),
                   InlineKeyboardButton('Katagana', callback_data=str(KATAKANA))],
                  [InlineKeyboardButton('Kembali', callback_data=str(ASING))]]