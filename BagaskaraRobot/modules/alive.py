import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from BagaskaraRobot.events import register
from BagaskaraRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/d8530063bb68cca946cd8.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hello guys!! [{event.sender.first_name}](tg://user?id={event.sender.id}), Im ʀᴇʏ ✘ ᴍᴜꜱɪᴄ.** \n\n"
  TEXT += "🔰 **Via aktif : sekarang** \n\n"
  TEXT += f"🔰 **My Master : [ʀᴇʏ](https://t.me/Rey_ab14)** \n\n"
  TEXT += f"🔰 **Library Version :** `{telever}` \n\n"
  TEXT += f"🔰 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"🔰 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Makasih yaa!! Sudah Mau Pakai ʀᴇʏ ✘ ᴍᴜꜱɪᴄ Disini 🙏**"
  BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/Rey_ab14musicbot"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/just_rey14"),
        ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
