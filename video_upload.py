from telegram import InputFile

def upload_video(bot, chat_id, video_file_path):
    with open(video_file_path, "rb") as video_file:
        bot.send_video(chat_id=chat_id, video=InputFile(video_file))
      
