from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Data import Data


home_filter = filters.create(lambda _, __, query: query.data.lower() == "home")
deploy_filter = filters.create(lambda _, __, query: query.data.lower() == "deploy")
about_filter = filters.create(lambda _, __, query: query.data.lower() == "about")
help_filter = filters.create(lambda _, __, query: query.data.lower() == "help")


# Callbacks
@Client.on_callback_query(home_filter)
async def _home(timebot, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    user = await timebot.get_me()
    mention = user["mention"]
    await timebot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=Data.START.format(callback_query.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )


@Client.on_callback_query(about_filter)
async def _about(timebot, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    await timebot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_button),
    )


@Client.on_callback_query(deploy_filter)
async def _deploy(timebot, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    await timebot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=Data.DEPLOY,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_button),
    )


@Client.on_callback_query(help_filter)
async def _help(timebot, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    await timebot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.help_buttons),
        parse_mode="Markdown"
    )
