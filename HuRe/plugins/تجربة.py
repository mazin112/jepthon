import asyncio
import os
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from HuRe import l313l
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import _catutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID
#lياعلي مدد
# جاي اشتغل عليه 😒

@l313l.on(admin_cmd(pattern=r"تيست (\d+)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    try:
        sleeptimet = sleeptimem = int(input_str[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    l313l = input_str[1:]
    await event.delete()
    addgvar("spamwork", True)
    await spam_function(event, reply, l313l, sleeptimem, sleeptimet, DelaySpam=True)


async def spam_function(event, HuRe, l313l, sleeptimem, sleeptimet, DelaySpam=False):
    counter = 0
    if len(l313l) == 2:
        spam_message = str(l313l[1])
        while gvarstatus("spamwork"):
            if event.reply_to_msg_id:
                await HuRe.reply(spam_message)
            counter += 1
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and HuRe.media:
        while gvarstatus("spamwork"):
            HuRe = await event.client.send_file(
                event.chat_id, HuRe, caption=HuRe.text
            )
            await _catutils.unsavegif(event, HuRe)
            counter += 1
            await asyncio.sleep(sleeptimem)
    
@l313l.ar_cmd(pattern="تعطيل التكرار")
async def stop_spam(event):
    delgvar("spamwork")
    await event.respond("**⌔∮ تم إيقاف التكرار بنجاح.**")
