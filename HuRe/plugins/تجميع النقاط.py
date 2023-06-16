#by Hussein For HuRe-HuRe
# IDK
# يمنع منعاً باتاً تخمط الملف خلي عندك كرامه ولتسرقة
from HuRe import l313l
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import requests
import re
import asyncio
from telethon import events
c = requests.session()
bot_username = '@zmmbot'
bot_username2 = '@A_MAN9300BOT'
bot_username3 = '@MARKTEBOT'
bot_username4 = '@qweqwe1919bot'
HuRe = ['yes']

@l313l.on(admin_cmd(pattern="(تجميع المليار|تجميع مليار)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username)
        await l313l.send_message('@zmmbot', '/start')
        await asyncio.sleep(3)
        msg0 = await l313l.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await l313l.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(1)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@l313l.on(admin_cmd(pattern="(تجميع الجوكر|تجميع جوكر)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت الجوكر , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username2)
        await l313l.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(2)
        msg0 = await l313l.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await l313l.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@l313l.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username3)
        await l313l.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await l313l.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await l313l.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(3)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@l313l.on(admin_cmd(pattern="(تجميع المليون|تجميع مليون)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await l313l.get_entity(bot_username4)
        await l313l.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await l313l.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await l313l.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await l313l.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await l313l(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await l313l.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await l313l.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await l313l.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

@l313l.on(admin_cmd(pattern="راتب وعد"))
async def hussein(event):
    if event.is_group:
        await event.edit("**᯽︙ تم تفعيل راتب وعد بنجاح سيتم أرسال راتب كل 11 دقيقة**")
        global is_active
        is_active_status = gvarstatus("is_active")
        if is_active_status != "True":
            addgvar("is_active", "True")
            await send_reham(event)
        else:
            await event.edit("**راتب وعد قيد التشغيل بالفعل!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def send_reham(event):
    is_active_status = gvarstatus("is_active")
    if is_active_status == "True":
        await event.respond('راتب')
        await asyncio.sleep(660)
        await send_reham(event)  
@l313l.on(admin_cmd(pattern="ايقاف راتب وعد"))
async def hussein(event):
    if event.is_group:
        delgvar("is_active")
        await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
@l313l.on(admin_cmd(pattern="بخشيش وعد"))
async def hussein(event):
    if event.is_group:
        await event.edit("**᯽︙ تم تفعيل بخشيش وعد بنجاح سيتم أرسال بخشيش كل 11 دقيقة**")
        global is_aljoker
        is_aljoker_status = gvarstatus("is_aljoker")
        if is_aljoker_status != "True":
            addgvar("is_aljoker", "True")
            await send_aljoker(event)
        else:
            await event.edit("**راتب وعد قيد التشغيل بالفعل!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def send_aljoker(event):
    is_aljoker_status = gvarstatus("is_aljoker")
    if is_aljoker_status == "True":
        await event.respond('بخشيش')
        await asyncio.sleep(660)
        await send_aljoker(event)  
@l313l.on(admin_cmd(pattern="ايقاف بخشيش وعد"))
async def hussein(event):
    if event.is_group:
        delgvar("is_aljoker")
        await event.edit("**᯽︙ تم تعطيل بخشيش وعد بنجاح ✅**")
    else:
        await event.edit("**᯽︙ هذا الأمر يمكن استخدامه فقط في المجموعات!**")
@l313l.on(admin_cmd(pattern="استثمار وعد(?:\s+(.*))?"))
async def hussein(event):
    if event.is_group:
        match = re.search(r"استثمار وعد(?:\s+(.*))?", event.raw_text)
        if match:
            message = match.group(1)
            if message:
                if message.isnumeric():
                    await event.edit(f"**᯽︙ تم تفعيل استثمار وعد بنجاح سيتم إرسال الرسالة '{message}' مع كلمة استثمار كل 10 دقائق**")
                    global its_hussein
                    its_hussein_status = gvarstatus("its_hussein")
                    if its_hussein_status != "True":
                        addgvar("its_hussein", "True")
                        await Reham_english(event, message)
                    else:
                        await event.edit("**استثمار وعد قيد التشغيل بالفعل!**")
                else:
                    await event.edit("**تنبيه: يجب أن يحتوي رقم الاستثمار على أرقام فقط!**")
            else:
                await event.edit("**تنبيه: يرجى كتابة رقم الاستثمار مع الأمر!**")
    else:
        await event.edit("**تنبيه: هذا الأمر يمكن استخدامه فقط في المجموعات!**")
async def Reham_english(event, message):
    its_hussein_status = gvarstatus("its_hussein")
    if its_hussein_status == "True":
        if message.isnumeric():
            await event.respond(f"استثمار {message}")
            await asyncio.sleep(660)
            await Reham_english(event, message)
        else:
            await event.respond("**تنبيه: يجب أن يحتوي رقم الاستثمار على أرقام فقط!**")
    else:
        if not message.isnumeric():
            await event.respond("**تنبيه: يجب أن يحتوي رقم الاستثمار على أرقام فقط!**")
@l313l.on(admin_cmd(pattern="ايقاف استثمار وعد"))
async def Reham(event):
    if event.is_group:
        its_hussein_status = gvarstatus("its_hussein")
        if its_hussein_status == "True":
            delgvar("its_hussein")
            await event.edit("**تم إيقاف استثمار الوعد بنجاح!**")
        else:
            await event.edit("**استثمار وعد ليست قيد التشغيل حاليًا!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

@l313l.on(admin_cmd(pattern="سرقة وعد(.*)"))
async def hussein(event):
    if event.is_group:
        message = event.pattern_match.group(1).strip()
        if message:
            await event.edit(f"**᯽︙ تم تفعيل سرقة وعد بنجاح سيتم إرسال الرسالة '{message}' مع كلمة سرقة كل 10 دقائق**")
            global its_reda
            its_reda_status = gvarstatus("its_reda")
            if its_reda_status != "True":
                addgvar("its_reda", "True")
                await send_message(event, message)
            else:
                await event.edit("**سرقة وعد قيد التشغيل بالفعل!**")
        else:
            await event.edit("**يرجى كتابة ايدي الشخص مع الامر!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

async def send_message(event, message):
    its_reda_status = gvarstatus("its_reda")
    if its_reda_status == "True":
        await event.respond(f"زرف {message}")
        await asyncio.sleep(660)
        await send_message(event, message)

@l313l.on(admin_cmd(pattern="ايقاف سرقة وعد"))
async def Reham(event):
    if event.is_group:
        its_reda_status = gvarstatus("its_reda")
        if its_reda_status == "True":
            delgvar("its_reda")
            await event.edit("**تم إيقاف سرقة الوعد بنجاح!**")
        else:
            await event.edit("**استثمار وعد ليست قيد التشغيل حاليًا!**")
    else:
        await event.edit("**هذا الأمر يمكن استخدامه فقط في المجموعات!**")

