from pyrogram import filters, Client
from config import OWNER_ID
from Yumikoo import Yumikoo
import random
from Yumikoo.Helper.database import *
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)



# ------------------------------------------------------------------------------- #


photo = [
"https://graph.org/file/2fc37c68163780e31599f.jpg",
"https://graph.org/file/3cc07627bdec5f5afab1c.jpg",
"https://graph.org/file/809fe233d8f7c29c6fd69.jpg",
"https://graph.org/file/677619500837cd3190c6d.jpg",
"https://graph.org/file/2a4d6cfdf60a38130aad2.jpg",
"https://graph.org/file/066ed5867fe94c333c0b6.jpg",
"https://graph.org/file/bd06b509e025bc656766d.jpg",
"https://graph.org/file/cd33fd3d193ac98486eff.jpg",
"https://graph.org/file/9ffb36ba7d53b7894eaba.jpg",
"https://graph.org/file/fe6dc66f7968ea69dcec0.jpg",
"https://graph.org/file/917d3b7324a056d66a8cb.jpg",
"https://graph.org/file/4f46ebdf26f703f1d5e93.jpg",
"https://graph.org/file/b3d7c31922a85e94e9627.jpg",
"https://graph.org/file/82560acb529e63c9ddb94.jpg",

]


@Yumikoo.on_message(group=10)
async def chat_watcher_func(_, message):
    try:
        if message.from_user:
            us_in_db = await is_served_user(message.from_user.id)
            if not us_in_db:
                await add_served_user(message.from_user.id)

        chat_id = (message.chat.id if message.chat.id != message.from_user.id else None)

        if not chat_id:
            return

        in_db = await is_served_chat(chat_id)
        if not in_db:
            await add_served_chat(chat_id)
    except:
        pass


# --------------------------------------------------------------------------------- #

@Yumikoo.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs** : `{chats}`
➻ **ᴜsᴇʀs** : `{users}`"""
    )
    
# --------------------------------------------------------------------------------- #


button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ ᴄʟᴏsᴇ ๏",callback_data="close_data")
        ]
    ])


# --------------------------------------------------------------------------------- #


@Yumikoo.on_message(filters.new_chat_members, group=2)
async def _kk(Yumikoo, message):
    chat = message.chat
    for members in message.new_chat_members:
        if members.id == 6691393517:
            count = await Yumikoo.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}"
            )
            await Yumikoo.send_photo(-1001802990747, photo=random.choice(photo), caption=msg, reply_markup=button)



