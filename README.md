# Telegram Video Downloader Bot

This Telegram bot allows users to download videos from supported OTT platforms. It supports premium features with limits on video downloads and provides admin functionalities to manage users.

## Features

- **Premium User Management**: Only premium users can download videos with download limits set by the admin.
- **Admin Commands**: Admin can manage premium users, broadcast messages, and more.
- **Video Quality Selection**: Users can select video quality and audio language before downloading.
- **Upload Features**: Videos can be uploaded directly on Telegram or Google Drive.
- **OTT Support**: The bot supports various OTT platforms (e.g., Netflix, Hotstar, MXPlayer, etc.).
  
## Available OTT Platforms
1. Aha
2. AmazonMiniTV
3. Atrangii
4. Crunchyroll
5. DangalPlay
6. EtvWin
7. Hoichoi
8. Hotstar
9. JioCinema
10. ManoramaMax
11. MXPlayer
12. Netflix
13. Platform8
14. PrimeVideo
15. Shemaroome
16. SonyLIV
17. Sunnxt
18. DiscoveryPlus
19. Zee5
20. Uulu

---

## Commands for Admins

- **`/add_premium <user_id> <videos> <days>`**: Add a user as premium with a specified number of videos and duration in days.
  - Example: `/add_premium 123456789 10 30` (Adds 10 videos for 30 days to the user with ID 123456789).
  
- **`/remove_premium <user_id>`**: Remove premium status from a user.
  - Example: `/remove_premium 123456789` (Removes premium access from the user with ID 123456789).

- **`/broadcast <message>`**: Send a message to all users of the bot.
  - Example: `/broadcast Hello users!` (Sends a broadcast message to all users).

- **`/stats`**: View total number of premium users.
  - Example: `/stats` (Displays stats for bot users).

- **`/bin_channel <channel_link>`**: Add a Telegram channel where users can receive downloaded video files directly.
  - Example: `/bin_channel https://t.me/my_channel` (Sets up a channel for video file distribution).

---

## Commands for Users

- **`/start`**: Start the bot and receive a welcome message.
  - Example: `/start` (Sends a welcome message to the user).

- **`/otts`**: List the available OTT platforms from which users can download videos.
  - Example: `/otts` (Lists the supported OTT platforms).

- **`/upgrade`**: Check the user’s current premium plan (video limit and duration).
  - Example: `/upgrade` (Displays the user’s video download plan).

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/telegram-bot.git
2. Install Dependencies: Navigate to the project directory and install the necessary Python packages:

bash
Copy code
pip install -r requirements.txt
Set Up Your Bot:

Open bot/config.py and replace the following:
BOT_TOKEN with the token from BotFather.
ADMIN_USER_ID with your admin Telegram user ID.
You can find your ADMIN_USER_ID by using @userinfobot on Telegram.
Run the Bot: After setting everything up, run the bot:

bash
Copy code
python main.py
Bot Flow
User Flow:

When a user starts the bot (/start), they receive a welcome message.
They can see available OTT platforms using the /otts command.
To upgrade to a premium plan, they can use the /upgrade command.
Admin Flow:

Admins can manage users with the /add_premium and /remove_premium commands.
Admins can broadcast messages to all users with /broadcast.
Admins can view bot statistics with /stats.
Admins can set up a Telegram channel for direct video distribution using /bin_channel.
Video Download Flow
Pre-Download Options:

Users choose the video quality and audio language before the download begins.
Download Process:

Only premium users can download videos, and they are limited to the number of downloads specified in their plan.
Admins can download unlimited videos without restrictions.
Video Upload:

Users and admins can upload videos directly to Telegram or Google Drive.
Post-Download:

After downloading, the video file is sent to the user via the bot, and admins can push the file to their "Bin Channel."
Additional Notes
Ensure the bot is used for legal purposes only.
This bot does not provide functionality for OTT platforms that require authentication or bypassing login mechanisms.
To manage your bot and update features, modify the relevant files within the bot/ folder.
Contributing
If you'd like to contribute to the bot, please fork the repository, make your changes, and submit a pull request.

License
This bot is for educational purposes only. Please make sure to follow all applicable laws and terms of service of the content providers.

yaml
Copy code

---

You can copy and paste this directly into your README.md file. Let me know if you need further adjustments!
