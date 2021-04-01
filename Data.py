from timebot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nI am a Time Teller bot which can tell time of any place (Not Wakanda :P). \nUse below buttons to get help or know more about me"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @MysteryBots ♥"

    # About Message
    ABOUT = "**About This Bot** \n\nThis is an open source Time bot by @MysteryBots \n\nSource : [Click Here](https://github.com/MysteryBots/TimeBot) \n\nFramework : [Pyrogram](docs.pyrogram.org) \n\nLanguage : [Python](www.python.org) \n\nDeveloper : [Mყʂƚҽɾყ Bσყ](https://t.me/MysteryxD)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Deploy Message
    DEPLOY = """
**Wanna create your own such bot??** 

This is simple and open source bot. 
Just click below on source code and tap on "Deploy to Heroku" to create your own bot. 

Click Here for [Source Code](https://github.com/MysteryBots/TimeBot)
"""

    HELP = """
**Need Help ?? **

Use below commands to follow me. I can be used everywhere including here, groups, channels and even inline mode so that you can use me in groups where I'm not present.

**Available Commands** :-
/time - `Time at present (defaults to India).`
/time <time zone> - `Time of that time zone at present.`
/timezones - `List all timezones.`
/search <continent/country/city> - `Search for timezone(s) for that continent/country/city.`
/gmt - `GMT time at present.`
/unixtime - `Unix Time at present. Same around the globe.`
/unix - `What is unix time?`
/about - `About this bot and source code.`
/help - `This Message.`
/start - `Check if bot is alive.`

**Inline Mode** :-
Format :- "`@TimeTellerBot <pass some text>`"
Use above format to use inline mode as follows:
- Pass no text or pass "time" to get current time.
- Pass any timezone to get that timezone's current time.
- Pass "gmt" to get current GMT time.
- Pass "unix" as text to get current unix time or learn 'What is unix ?'

**Support** - @MysteryBots & @MysteryBotsChat
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Help Buttons
    help_buttons = [
        [InlineKeyboardButton("📤 Inline Mode 📤", switch_inline_query="")],
        [
            InlineKeyboardButton("⏳ Time ⏳", switch_inline_query_current_chat="time"),
            InlineKeyboardButton("🏮 Time Zone 🏮", switch_inline_query_current_chat="America/Detroit"),
        ],
        [
            InlineKeyboardButton("⛓ Unix ⛓", switch_inline_query_current_chat="unix"),
            InlineKeyboardButton("💰 GMT 💰", switch_inline_query_current_chat="gmt"),
        ],
        [InlineKeyboardButton("🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("📤 About 📤", callback_data="about"),
        ],
        [
            InlineKeyboardButton("⏳ Time ⏳", switch_inline_query_current_chat="time"),
            InlineKeyboardButton("💌 Inline Mode 💌", switch_inline_query=""),
        ],
        [InlineKeyboardButton("Create your own bot", callback_data="deploy")],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/MysteryBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/MysteryBotsChat")],
    ]
