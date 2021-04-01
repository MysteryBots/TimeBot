import datetime
from pyrogram import Client, filters


@Client.on_message(filters.command(["timezones"]))
async def timezones(time, msg):
    await msg.reply_document("timezones.txt", quote=True)