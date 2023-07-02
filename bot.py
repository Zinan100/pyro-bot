from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(
  "Zinan",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)


@app.on_mesage(filters.command('start'))
async def start_msg(Message: msg):
  await msg.reply_text("hi guys")


app.run()
