from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# About Message
@Client.on_message(filters.command(["about"]))
async def about(timebot, msg):
    await msg.reply(
        text=Data.ABOUT,
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(Data.home_button),
    )