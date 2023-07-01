from HuRe import l313l
from datetime import datetime
from telethon.errors import FloodWaitError
import asyncio
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import AUTONAME, edit_delete, l313l, logging
normzltext = "1234567890"
namerzfont = Config.JP_FN or "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
autoname_task = None

async def autoname_loop():
    global autoname_task
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        current_time = datetime.now().strftime("%H:%M:%S")
        for normal in current_time:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                current_time = current_time.replace(normal, namefont)
        name = f"{lMl10l} {current_time}"
        LOGS.info(name)
        try:
            await l313l(functions.account.UpdateProfileRequest(last_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(120)
        await asyncio.sleep(1)
        AUTONAMESTART = gvarstatus("autoname") == "true"

@l313l.on(admin_cmd(pattern=f"اسم ثواني(?:\s|$)([\s\S]*)"))
async def _(event):
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, "**الاسـم الـوقتي شغـال بالأصـل 🧸♥**")
    addgvar("autoname", True)
    await edit_delete(event, "**تم تفـعيل اسـم الـوقتي بنجـاح ✓**")
    if autoname_task is None:
        autoname_task = asyncio.create_task(autoname_loop())

@l313l.on(admin_cmd(pattern="ايقاف ثواني$"))
async def _(event):
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        delgvar("autoname")
        if autoname_task is not None:
            autoname_task.cancel()
            autoname_task = None
        await edit_delete(event, "**تم تعطيل اسـم الـوقتي بنجـاح ✓**")
    else:
        await edit_delete(event, "**اسـم الـوقتي معطـل بـالأصـل ❗**")