import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ContextTypes
)

# لاگ‌گیری برای بررسی خطاها
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# توکن ربات
TOKEN = '7047420506:AAEdan-l2Cb6h9sgKv5R9mLIubbqw7dgoDU'

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['/startbot']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("برای شروع روی /startbot بزن", reply_markup=reply_markup)

# شروع اصلی بعد از عضویت
async def startbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['عضو شدم✅️']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "سلام خوش اومدی\n"
        "قبل از اینکه شروع کنیم در کانال ما عضو شو و سپس روی \n"
        "عضو شدم✅️ کلیک کن تا به خدمات دسترسی پیدا کنی\n"
        "👇 https://t.me/+CVwJnJR7KhdiZDM0",
        reply_markup=reply_markup
    )

# هندل پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip()

        if text == 'عضو شدم✅️':
            keyboard = [['تبدیل عکس به ویدیو'], ['کاهش حجم ویدیو'], ['ارتباط با پشتیبانی']]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text("چطور می‌تونم کمکت کنم؟", reply_markup=reply_markup)

        elif text == 'تبدیل عکس به ویدیو':
            await update.message.reply_text(
                "هزینه تبدیل عکس به ویدیو ۱۵ هزار تومنه. لطفاً:\n"
                "۱. عکس مورد نظر\n"
                "۲. توضیحات کوتاه\n"
                "۳. رسید واریزی\n"
                "رو به این آیدی بفرست:\n@Videomakeradmin\n"
                "کارت: ۶۰۶۳۷۳۱۱۸۵۶۵۵۸۳۵ - محمد بارانی لنبانی"
            )

        elif text == 'کاهش حجم ویدیو':
            await update.message.reply_text(
                "هزینه کاهش حجم ویدیو ۵ هزار تومنه. لطفاً:\n"
                "۱. ویدیوی مورد نظر\n"
                "۲. رسید واریزی\n"
                "رو به این آیدی بفرست:\n@Videomakeradmin\n"
                "کارت: ۶۰۶۳۷۳۱۱۸۵۶۵۵۸۳۵ - محمد بارانی لنبانی"
            )

        elif text == 'ارتباط با پشتیبانی':
            await update.message.reply_text("آیدی پشتیبانی:\n@Videomakeradmin")

    except Exception as e:
        logging.error(f"خطا در handle_message: {e}")
        await update.message.reply_text("یه مشکلی پیش اومده. لطفاً دوباره امتحان کن.")

# اجرای برنامه
if __name__ == '__main__':
    try:
        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("startbot", startbot))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        print("ربات با موفقیت اجرا شد و در حال گوش دادن است...")
        app.run_polling()

    except Exception as e:
        logging.critical(f"خطای کلی برنامه: {e}")