from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = """
You Can Contact me :- [Click Here](https://t.me/darks_cat_bot)
Plzz Follow me on [github](https://github.com/DARKEMPIRESL)😁😎
Please Subscribe Our [Chanel](https://t.me/SLBotOfficial) 😎🔰
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup(
        [   
            [InlineKeyboardButton("CRICKET NEWS", url="https://t.me/THE_CRICKET_WORLD_NEWS"),InlineKeyboardButton("Contact Owner", url=f"https://t.me/darks_cat_bot")],
            [InlineKeyboardButton("Support Group", url="https://t.me/trtechguide"),InlineKeyboardButton("Support Chanel", url="https://t.me/SLBotOfficial"),InlineKeyboardButton("Github", url=f"https://github.com/DARKEMPIRESL")],
        ]       
)


@Client.on_message(filters.command("start"))
async def start(client, message):
    fuser = message.from_user.id
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    NewVar = START
    if var.OWNER_ID and not message.from_user.id == var.OWNER_ID:
        geto = await client.get_users(var.OWNER_ID)
        NewVar += f"\n\nMaintained By {geto.mention}"
    else:
        NewVar += "\n**Onwer Commands** - https://te.legra.ph/Owner-Commands-04-03-9"
    await message.reply_text(
        NewVar, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )
