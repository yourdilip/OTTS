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
