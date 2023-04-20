import openai
from HuRe import l313l
from ..core.managers import edit_or_reply
from telethon import events

@l313l.on(admin_cmd(pattern="ذكاء(?:\s|$)([\s\S]*)"))
async def chatgptjk(event):
    await edit_or_reply(event, "@jepthon")
