from time import sleep
from logging import basicConfig
from telegram import *
from telegram.ext import *
from PTB_PKG import *

def main():
    updater = Updater(token='1708137883:AAEisJWKr-xRygtm3GC9zq9oDDTq_P3215E', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(
        ConversationHandler(
            entry_points=[
                CommandHandler('start', start)],
            states={
                CYMAP:[
                    CallbackQueryHandler(masuk_ke_bot_go, pattern=str(DUKUNGAN)),
                    CallbackQueryHandler(masuk_ke_bot_back, pattern=str(MASUK_KE_BOT_BACK)),
                    CallbackQueryHandler(rekoba_go, pattern=str(REKOBA)),
                    CallbackQueryHandler(asing_go, pattern=str(ASING)),
                    CallbackQueryHandler(jepang_go, pattern=str(JEPANG)),
                    CallbackQueryHandler(jepang_kanji, pattern=str(KANJI)),
                    CallbackQueryHandler(jepang_hiragana, pattern=str(HIRAGANA)),
                    CallbackQueryHandler(jepang_katakana, pattern=str(KATAKANA)),
                    CallbackQueryHandler(malaysia, pattern=str(MALAYSIA)),
                    CallbackQueryHandler(inggris, pattern=str(INGGRIS)),
                    CallbackQueryHandler(arab, pattern=str(ARAB)),
                    CallbackQueryHandler(korea, pattern=str(KOREA)),
                    CallbackQueryHandler(jerman, pattern=str(JERMAN)),
                    CallbackQueryHandler(rusia, pattern=str(RUSIA)),
                    CallbackQueryHandler(belanda, pattern=str(BELANDA)),
                    CallbackQueryHandler(china, pattern=str(CHINA)),
                    CallbackQueryHandler(thailand, pattern=str(THAILAND)),
                    CallbackQueryHandler(myanmar, pattern=str(MYANMAR)),
                    CallbackQueryHandler(india, pattern=str(INDIA)),
                    CallbackQueryHandler(lokal_go, pattern=str(LOKAL)),
                    CallbackQueryHandler(jawa, pattern=str(JAWA)),
                    CallbackQueryHandler(sunda, pattern=str(SUNDA)),
                    CallbackQueryHandler(madura, pattern=str(MADURA)),
                    CallbackQueryHandler(betawi, pattern=str(BETAWI)),
                    CallbackQueryHandler(bugis, pattern=str(BUGIS)),
                    CallbackQueryHandler(minangkabau, pattern=str(MINANGKABAU)),
                    CallbackQueryHandler(banjar, pattern=str(BANJAR)),
                    CallbackQueryHandler(aceh, pattern=str(ACEH)),
                    CallbackQueryHandler(bali, pattern=str(BALI)),
                    CallbackQueryHandler(palembang, pattern=str(PALEMBANG)),
                    CallbackQueryHandler(repeti_go, pattern=str(REPETI)),
                    CallbackQueryHandler(reuni_go, pattern=str(REUNI)),],
                PTB_KANJI:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), kanji_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), kanji_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, kanji_text),
                    MessageHandler(Filters.sticker, kanji_sticker),
                    MessageHandler(Filters.voice, kanji_voice),
                    MessageHandler(Filters.photo, kanji_photo),
                    MessageHandler(Filters.video, kanji_video),
                    MessageHandler(Filters.video_note, kanji_video_note),
                    MessageHandler(Filters.invoice, kanji_invoice)],
                PTB_HIRAGANA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), hiragana_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), hiragana_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, hiragana_text),
                    MessageHandler(Filters.sticker, hiragana_sticker),
                    MessageHandler(Filters.voice, hiragana_voice),
                    MessageHandler(Filters.photo, hiragana_photo),
                    MessageHandler(Filters.video, hiragana_video),
                    MessageHandler(Filters.video_note, hiragana_video_note),
                    MessageHandler(Filters.invoice, hiragana_invoice)],
                PTB_KATAKANA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), katakana_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), katakana_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, katakana_text),
                    MessageHandler(Filters.sticker, katakana_sticker),
                    MessageHandler(Filters.voice, katakana_voice),
                    MessageHandler(Filters.photo, katakana_photo),
                    MessageHandler(Filters.video, katakana_video),
                    MessageHandler(Filters.video_note, katakana_video_note),
                    MessageHandler(Filters.invoice, katakana_invoice)],
                PTB_MALAYSIA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), malaysia_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), malaysia_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, malaysia_text),
                    MessageHandler(Filters.sticker, malaysia_sticker),
                    MessageHandler(Filters.voice, malaysia_voice),
                    MessageHandler(Filters.photo, malaysia_photo),
                    MessageHandler(Filters.video, malaysia_video),
                    MessageHandler(Filters.video_note, malaysia_video_note),
                    MessageHandler(Filters.invoice, malaysia_invoice)],
                PTB_INGGRIS:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), inggris_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), inggris_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, inggris_text),
                    MessageHandler(Filters.sticker, inggris_sticker),
                    MessageHandler(Filters.voice, inggris_voice),
                    MessageHandler(Filters.photo, inggris_photo),
                    MessageHandler(Filters.video, inggris_video),
                    MessageHandler(Filters.video_note, inggris_video_note),
                    MessageHandler(Filters.invoice, inggris_invoice)],
                PTB_ARAB:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), arab_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), arab_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, arab_text),
                    MessageHandler(Filters.sticker, arab_sticker),
                    MessageHandler(Filters.voice, arab_voice),
                    MessageHandler(Filters.photo, arab_photo),
                    MessageHandler(Filters.video, arab_video),
                    MessageHandler(Filters.video_note, arab_video_note),
                    MessageHandler(Filters.invoice, arab_invoice)],
                PTB_KOREA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), korea_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), korea_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, korea_text),
                    MessageHandler(Filters.sticker, korea_sticker),
                    MessageHandler(Filters.voice, korea_voice),
                    MessageHandler(Filters.photo, korea_photo),
                    MessageHandler(Filters.video, korea_video),
                    MessageHandler(Filters.video_note, korea_video_note),
                    MessageHandler(Filters.invoice, korea_invoice)],
                PTB_JERMAN:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), jerman_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), jerman_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, jerman_text),
                    MessageHandler(Filters.sticker, jerman_sticker),
                    MessageHandler(Filters.voice, jerman_voice),
                    MessageHandler(Filters.photo, jerman_photo),
                    MessageHandler(Filters.video, jerman_video),
                    MessageHandler(Filters.video_note, jerman_video_note),
                    MessageHandler(Filters.invoice, jerman_invoice)],
                PTB_RUSIA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), rusia_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), rusia_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, rusia_text),
                    MessageHandler(Filters.sticker, rusia_sticker),
                    MessageHandler(Filters.voice, rusia_voice),
                    MessageHandler(Filters.photo, rusia_photo),
                    MessageHandler(Filters.video, rusia_video),
                    MessageHandler(Filters.video_note, rusia_video_note),
                    MessageHandler(Filters.invoice, rusia_invoice)],
                PTB_BELANDA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), belanda_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), belanda_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, belanda_text),
                    MessageHandler(Filters.sticker, belanda_sticker),
                    MessageHandler(Filters.voice, belanda_voice),
                    MessageHandler(Filters.photo, belanda_photo),
                    MessageHandler(Filters.video, belanda_video),
                    MessageHandler(Filters.video_note, belanda_video_note),
                    MessageHandler(Filters.invoice, belanda_invoice)],
                PTB_CHINA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), china_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), china_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, china_text),
                    MessageHandler(Filters.sticker, china_sticker),
                    MessageHandler(Filters.voice, china_voice),
                    MessageHandler(Filters.photo, china_photo),
                    MessageHandler(Filters.video, china_video),
                    MessageHandler(Filters.video_note, china_video_note),
                    MessageHandler(Filters.invoice, china_invoice)],
                PTB_THAILAND:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), thailand_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), thailand_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, thailand_text),
                    MessageHandler(Filters.sticker, thailand_sticker),
                    MessageHandler(Filters.voice, thailand_voice),
                    MessageHandler(Filters.photo, thailand_photo),
                    MessageHandler(Filters.video, thailand_video),
                    MessageHandler(Filters.video_note, thailand_video_note),
                    MessageHandler(Filters.invoice, thailand_invoice)],
                PTB_MYANMAR:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), myanmar_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), myanmar_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, myanmar_text),
                    MessageHandler(Filters.sticker, myanmar_sticker),
                    MessageHandler(Filters.voice, myanmar_voice),
                    MessageHandler(Filters.photo, myanmar_photo),
                    MessageHandler(Filters.video, myanmar_video),
                    MessageHandler(Filters.video_note, myanmar_video_note),
                    MessageHandler(Filters.invoice, myanmar_invoice)],
                PTB_INDIA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), india_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), india_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, india_text),
                    MessageHandler(Filters.sticker, india_sticker),
                    MessageHandler(Filters.voice, india_voice),
                    MessageHandler(Filters.photo, india_photo),
                    MessageHandler(Filters.video, india_video),
                    MessageHandler(Filters.video_note, india_video_note),
                    MessageHandler(Filters.invoice, india_invoice)],
                
                PTB_JAWA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), jawa_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), jawa_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, jawa_text),
                    MessageHandler(Filters.sticker, jawa_sticker),
                    MessageHandler(Filters.voice, jawa_voice),
                    MessageHandler(Filters.photo, jawa_photo),
                    MessageHandler(Filters.video, jawa_video),
                    MessageHandler(Filters.video_note, jawa_video_note),
                    MessageHandler(Filters.invoice, jawa_invoice)],
                PTB_SUNDA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), sunda_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), sunda_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, sunda_text),
                    MessageHandler(Filters.sticker, sunda_sticker),
                    MessageHandler(Filters.voice, sunda_voice),
                    MessageHandler(Filters.photo, sunda_photo),
                    MessageHandler(Filters.video, sunda_video),
                    MessageHandler(Filters.video_note, sunda_video_note),
                    MessageHandler(Filters.invoice, sunda_invoice)],
                PTB_MADURA:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), madura_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), madura_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, madura_text),
                    MessageHandler(Filters.sticker, madura_sticker),
                    MessageHandler(Filters.voice, madura_voice),
                    MessageHandler(Filters.photo, madura_photo),
                    MessageHandler(Filters.video, madura_video),
                    MessageHandler(Filters.video_note, madura_video_note),
                    MessageHandler(Filters.invoice, madura_invoice)],
                PTB_BETAWI:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), betawi_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), betawi_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, betawi_text),
                    MessageHandler(Filters.sticker, betawi_sticker),
                    MessageHandler(Filters.voice, betawi_voice),
                    MessageHandler(Filters.photo, betawi_photo),
                    MessageHandler(Filters.video, betawi_video),
                    MessageHandler(Filters.video_note, betawi_video_note),
                    MessageHandler(Filters.invoice, betawi_invoice)],
                PTB_BUGIS:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), bugis_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), bugis_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, bugis_text),
                    MessageHandler(Filters.sticker, bugis_sticker),
                    MessageHandler(Filters.voice, bugis_voice),
                    MessageHandler(Filters.photo, bugis_photo),
                    MessageHandler(Filters.video, bugis_video),
                    MessageHandler(Filters.video_note, bugis_video_note),
                    MessageHandler(Filters.invoice, bugis_invoice)],
                PTB_MINANGKABAU:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), minangkabau_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), minangkabau_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, minangkabau_text),
                    MessageHandler(Filters.sticker, minangkabau_sticker),
                    MessageHandler(Filters.voice, minangkabau_voice),
                    MessageHandler(Filters.photo, minangkabau_photo),
                    MessageHandler(Filters.video, minangkabau_video),
                    MessageHandler(Filters.video_note, minangkabau_video_note),
                    MessageHandler(Filters.invoice, minangkabau_invoice)],
                PTB_BANJAR:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), banjar_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), banjar_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, banjar_text),
                    MessageHandler(Filters.sticker, banjar_sticker),
                    MessageHandler(Filters.voice, banjar_voice),
                    MessageHandler(Filters.photo, banjar_photo),
                    MessageHandler(Filters.video, banjar_video),
                    MessageHandler(Filters.video_note, banjar_video_note),
                    MessageHandler(Filters.invoice, banjar_invoice)],
                PTB_ACEH:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), aceh_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), aceh_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, aceh_text),
                    MessageHandler(Filters.sticker, aceh_sticker),
                    MessageHandler(Filters.voice, aceh_voice),
                    MessageHandler(Filters.photo, aceh_photo),
                    MessageHandler(Filters.video, aceh_video),
                    MessageHandler(Filters.video_note, aceh_video_note),
                    MessageHandler(Filters.invoice, aceh_invoice)],
                PTB_BALI:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), bali_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), bali_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, bali_text),
                    MessageHandler(Filters.sticker, bali_sticker),
                    MessageHandler(Filters.voice, bali_voice),
                    MessageHandler(Filters.photo, bali_photo),
                    MessageHandler(Filters.video, bali_video),
                    MessageHandler(Filters.video_note, bali_video_note),
                    MessageHandler(Filters.invoice, bali_invoice)],
                PTB_PALEMBANG:[
                    MessageHandler(Filters.command | Filters.regex('Mencari'), palembang_find),
                    MessageHandler(Filters.command | Filters.regex('Berhenti'), palembang_disconnect),
                    MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), masuk_ke_bot),
                    MessageHandler(Filters.text, palembang_text),
                    MessageHandler(Filters.sticker, palembang_sticker),
                    MessageHandler(Filters.voice, palembang_voice),
                    MessageHandler(Filters.photo, palembang_photo),
                    MessageHandler(Filters.video, palembang_video),
                    MessageHandler(Filters.video_note, palembang_video_note),
                    MessageHandler(Filters.invoice, palembang_invoice)]},
            
            fallbacks=[CommandHandler('start', start)]))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()