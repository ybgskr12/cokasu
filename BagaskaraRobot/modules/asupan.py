# ⚠️ © @greyyvbss 
# ⚠️ Don't Remove Credits

import os
import random
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo
from BagaskaraRobot.events import register
from BagaskaraRobot import telethn as tbot, ubot2                 


@register(pattern="^/asupan ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Video Asupan...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@asupancilikbot", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Asupan nya Kak 🥵", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  


@register(pattern="^/ayang ?(.*)")
async def _(event):
    bubur = await event.reply("**Mencari Ayang...🔍**") 
    try:
        ayangnya = [
            ayang
            async for ayang in ubot2.iter_messages(
            "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        termos = random.choice(ayangnya)
        kompor = await ubot2.download_media(termos)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Ayang nya Kak ♥️💘💝💖💗💞🙀", 
            file=kompor
            )
        await bubur.delete()
    except Exception:
        await bubur.edit("Ayangnya Gada Karena Lu Jelek")  

        
@register(pattern="^/ppcp ?(.*)")
async def _(event):
    liong = await event.reply("**Mencari PP Couple...🔍**") 
    try:
        couplenya = [
            couple
            async for couple in ubot2.iter_messages(
            "@ppcpcilik", filter=InputMessagesFilterPhotos
            )
        ]
        kopi = random.choice(couplenya)
        roko = await ubot2.download_media(kopi)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Kak PP Couplenya😍", 
            file=roko
            )
        await liong.delete()
    except Exception:
        await liong.edit("PP Couple Ny Gada Yang Bagus _-")  
        

__mod_name__ = "Asupan"

        
