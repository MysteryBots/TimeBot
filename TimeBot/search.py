import pytz
from pyrogram import Client, filters


@Client.on_message(filters.command(["search"]))
async def search(timebot, msg):
    if len(msg.command) == 1:
        pass
    elif len(msg.command) == 2:
        location = (msg.command[1]).capitalize()
        tz = []
        for line in pytz.all_timezones:
            words = line.split("/")
            if location in words:
                tz.append(line)
        if len(tz) > 0:
            if len(tz) == 1:
                string = f"**Timezone Found** : `{tz[0]}`"
            else:
                string = "**Timezones Found** \n\n"
                n = 0
                for t in tz:
                    n += 1
                    string += f"{n})  `{t}`\n"
            await msg.reply(string, quote=True)
        else:
            await msg.reply("No Such Timezone Found \n\n<i>If you believe this is wrong then contact us at @MysteryBotsChat</i>", quote=True)