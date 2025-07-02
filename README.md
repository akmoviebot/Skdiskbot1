# Skdiskbot

Telegram bot to upload files & generate short links via exe.io.

## ⚙️ Setup

1. Create bot via BotFather → get BOT_TOKEN.
2. Make Telegram channel → set LOG_CHANNEL (e.g., @skdiskbotfile).
3. Register at exe.io → get SHORTENER_API token.
4. Get API_ID & API_HASH from my.telegram.org.
5. Create `.env` with:
   ```
   BOT_TOKEN=...
   API_ID=...
   API_HASH=...
   LOG_CHANNEL=@skdiskbotfile
   SHORTENER_API=...
   ```
6. Deploy on Heroku/Railway.

## 🚀 Commands

- `/start` to begin.
- Send any file → get short link + auto-post in channel.
