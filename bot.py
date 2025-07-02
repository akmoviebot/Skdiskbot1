import os, requests, logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Config (environment variables)
BOT_TOKEN = os.getenv("")
API_ID = int(os.getenv("27084955"))
API_HASH = os.getenv("91c88b554ab2a34f8b0c72228f06fc0b")
LOG_CHANNEL = os.getenv("-1002269022170")
SHORTENER_API = os.getenv("9deac3bf344cd8a3724e99f0af8c87e13079cb01")
SHORTENER_URL = f"https://exe.io/api?api={SHORTENER_API}&url={{}}"

logging.basicConfig(level=logging.INFO)
bot = Client("skdiskbot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.command("start"))
async def start_handler(_, m):
    await m.reply_text(
      f"Hi {m.from_user.first_name}! Send me a file, I’ll generate a short link for you.",
      reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel 📢", url=f"https://t.me/{LOG_CHANNEL.strip('@')}")]
      ])
    )

@bot.on_message(filters.document | filters.video | filters.audio)
async def file_handler(_, m):
    msg = await m.reply("🔄 Uploading & shortening…")
    f = await m.download()
    short_url = requests.get(SHORTENER_URL.format(f"https://telegra.ph/{os.path.basename(f)}")).json().get("shortenedUrl")
    if not short_url:
        return await msg.edit("❌ Link shortening failed.")
    await bot.send_document(LOG_CHANNEL, document=f, caption=f"**{m.document.file_name}**\n📥 [Download]({short_url})")
    await msg.edit(f"✅ Here’s your link:\n{short_url}")
    os.remove(f)

bot.run()
