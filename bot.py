from pyrogram import Client, filters

# Your Bot's token (get this from BotFather)
api_id = "YOUR_API_ID"  # Get this from my.telegram.org
api_hash = "YOUR_API_HASH"  # Get this from my.telegram.org
bot_token = "YOUR_BOT_TOKEN"  # Get this from BotFather

# Initialize Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# /start command handler
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello, I am your bot! How can I assist you today?")

# /help command handler
@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply("Use /start to begin and other commands as needed.")

# /echo command handler
@app.on_message(filters.command("echo"))
async def echo(client, message):
    # Echoes back the text sent by the user
    await message.reply(message.text)

# /sendfile command to send a file
@app.on_message(filters.command("sendfile"))
async def send_file(client, message):
    # Replace 'path_to_file' with the actual file path or URL
    await message.reply_document("path_to_file")

# Run the bot
app.run()
  
