from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot.config import BOT_TOKEN, ADMIN_USER_ID
from bot.user_management import add_premium, remove_premium, check_premium_status, get_stats
from bot.downloader import download_video
from bot.video_upload import upload_video

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your video downloader bot. Use /otts to see available platforms.")

def otts(update: Update, context: CallbackContext):
    available_otts = [
        "Aha", "AmazonMiniTV", "Atrangii", "Crunchyroll", "DangalPlay", 
        "EtvWin", "Hoichoi", "Hotstar", "JioCinema", "ManoramaMax", 
        "MXPlayer", "Netflix", "Platform8", "PrimeVideo", "Shemaroome", 
        "SonyLIV", "Sunnxt", "DiscoveryPlus", "Zee5", "Uulu"
    ]
    update.message.reply_text("Available OTT platforms: " + ", ".join(available_otts))

def upgrade(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in check_premium_status():
        status = check_premium_status()[user_id]
        update.message.reply_text(f"Your plan: {status['videos']} videos for {status['days']} days.")
    else:
        update.message.reply_text("You are not a premium user. Please upgrade your plan.")

def add_premium_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_USER_ID:
        user_id = int(context.args[0])
        days = int(context.args[1])
        videos = int(context.args[2])
        add_premium(user_id, videos, days)
        update.message.reply_text(f"Added premium status to user {user_id}. {videos} videos for {days} days.")
    else:
        update.message.reply_text("You are not authorized to perform this action.")

def remove_premium_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_USER_ID:
        user_id = int(context.args[0])
        remove_premium(user_id)
        update.message.reply_text(f"Removed premium status from user {user_id}.")
    else:
        update.message.reply_text("You are not authorized to perform this action.")

def stats_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_USER_ID:
        stats = get_stats()
        update.message.reply_text(f"Total bot users: {stats['total_users']}")
    else:
        update.message.reply_text("You are not authorized to perform this action.")

def handle_video_request(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in check_premium_status():
        # Fetching the premium status and video limit
        user_status = check_premium_status()[user_id]
        video_url = update.message.text
        if user_status['videos'] > 0:
            # Deduct one video from the user's limit
            download_video(video_url, user_id)
            user_status['videos'] -= 1
            update.message.reply_text("Downloading video for you!")
        else:
            update.message.reply_text("You've reached your download limit!")
    else:
        update.message.reply_text("You need to be a premium user to download videos!")

def start_bot():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("otts", otts))
    dp.add_handler(CommandHandler("upgrade", upgrade))
    dp.add_handler(CommandHandler("add_premium", add_premium_command))
    dp.add_handler(CommandHandler("remove_premium", remove_premium_command))
    dp.add_handler(CommandHandler("stats", stats_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_video_request))
    updater.start_polling()
    updater.idle()
      
