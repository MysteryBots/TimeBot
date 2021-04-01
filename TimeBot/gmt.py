import pytz
from pyrogram import Client, filters
from TimeBot import TimeTeller


# GMT Time
@Client.on_message(filters.command("gmt"))
async def gmt_time(timebot, msg):
    time = TimeTeller.gmt()
    await msg.reply(time, quote=True)