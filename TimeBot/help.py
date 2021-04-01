from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.command("help"))
async def _help(timebot, msg):
    await timebot.send_message(
        chat_id=msg.chat.id,
        text=Data.HELP,
        disable_notification=True,
        reply_markup=InlineKeyboardMarkup(Data.help_buttons),
        parse_mode="Markdown"
    )
