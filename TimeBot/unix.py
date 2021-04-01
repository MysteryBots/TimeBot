from pyrogram import Client, filters


@Client.on_message(filters.command(["unix"]))
async def unix(timebot, msg):
    await msg.reply(what, disable_web_page_preview=True, quote=True)
   

# https://stackoverflow.com/a/20823376/15439106
what = "The Unix timestamp is a way to track time as a running total of seconds. This count starts at the Unix Epoch on January 1st, 1970 at UTC. Therefore, **the Unix timestamp is merely the number of seconds between a particular date and the Unix Epoch.** It should also be pointed out that this point in time technically does not change no matter where you are located on the globe. This is very useful to computer systems for tracking and sorting dated information in dynamic and distributed applications both online and client-side. The reason why Unix timestamps are used by many webmasters is that they can represent all time zones at once. For more information, read the [Wikipedia article](http://en.wikipedia.org/wiki/Unix_time)."