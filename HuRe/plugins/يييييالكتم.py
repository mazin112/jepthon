import base64
import asyncio
from datetime import datetime
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights
from telethon.utils import get_display_name
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

from HuRe import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format
from ..sql_helper import gban_sql_helper as gban_sql
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, admin_groups, get_user_from_event
#ياعلي مدد 313
#علي مع الحق والحق مع علي يدور معهُ حينما دار
plugin_category = "admin"
muted_users = []
joker_mute = "https://telegra.ph/file/c5ef9550465a47845c626.jpg"
joker_unmute = "https://telegra.ph/file/e9473ddef0b58cdd7f9e7.jpg"
#=================== الكـــــــــــــــتم  ===================  #
muted_users_variable = "muted_users"
if gvarstatus(muted_users_variable) is None:
    addgvar(muted_users_variable)

@l313l.ar_cmd(pattern=r"كتم(?:\s|$)([\s\S]*)")
async def mute_aljoker(event):
    await event.delete()
    muted_users_variable = "muted_users"
    muted_users_str = gvarstatus(muted_users_variable)
    if muted_users_str is None:
        muted_users = []
    else:
        muted_users = eval(muted_users_str)
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
        if is_muted(event.chat_id, event.chat_id):
            return await event.edit("**- هذا المستخدم مكتوم سابقًا.**")
        if event.chat_id == l313l.uid:
            return await edit_delete(event, "**- لماذا تريد كتم نفسك؟**")
        if event.chat_id == 705475246:
            return await edit_delete(event, "**- لا يمكنني كتم مطور السورس.**")
        try:
            mute(event.chat_id, event.chat_id)
            muted_users.append(replied_user.id)
        except Exception as e:
            await event.edit(f"**- حدث خطأ: {e}**")
        else:
            profile_link = f"[{replied_user.first_name}](tg://user?id={event.chat_id})"
            return await event.client.send_file(
                event.chat_id,
                joker_mute,
                caption=f"**تم كتم المستخدم بنجاح.**\n\n**- المستخدم:** {profile_link}",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#كتم_الخاص\n"
                f"**- الشخص:** {profile_link}\n",
            )
    else:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return await edit_or_reply(
                event, "**أنا لست مشرف هنا.**"
            )
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == l313l.uid:
            return await edit_or_reply(event, "**- لماذا تريد كتم نفسك؟**")
        if user.id == 705475246:
            return await edit_or_reply(event, "**- لا يمكنني كتم مطور السورس.**")
        if is_muted(user.id, event.chat_id):
            return await edit_or_reply(
                event, "**- هذا الشخص مكتوم سابقًا هنا.**"
            )
        result = await event.client.get_permissions(event.chat_id, user.id)
        try:
            if result.participant.banned_rights.send_messages:
                return await edit_or_reply(
                    event,
                    "**- هذا الشخص مكتوم سابقًا هنا.**",
                )
        except AttributeError:
            pass
        except Exception as e:
            return await edit_or_reply(event, f"**- حدث خطأ: {e}**")
        try:
            mute(user.id, event.chat_id)
            muted_users.append(user.id)
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await edit_or_reply(
                        event,
                        "**- عذرًا، ليس لديك صلاحية حذف الرسائل هنا.**",
                    )
            elif "creator" not in vars(chat):
                return await edit_or_reply(
                    event, "**- عذرًا، ليس لديك صلاحية حذف الرسائل هنا.**"
                )
        except Exception as e:
            return await edit_or_reply(event, f"**- حدث خطأ: {e}**")
        profile_link = f"[{user.first_name}](tg://user?id={user.id})"
        if reason:
            await event.client.send_file(
                event.chat_id,
                joker_mute,
                caption=f"**- المستخدم:** {profile_link}\n**- تم كتمه بنجاح.**\n\n**- السبب:** {reason}",
            )
        else:
            await event.client.send_file(
                event.chat_id,
                joker_mute,
                caption=f"**- المستخدم:** {profile_link}\n**- تم كتمه بنجاح.**\n\n",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
            "#الكتم\n"    
                f"**- الشخص:** [{user.first_name}](tg://user?id={user.id})\n"
                f"**- الدردشة:** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )
    
#=================== الغـــــــــــــاء الكـــــــــــــــتم  ===================  #

@l313l.ar_cmd(pattern=r"(الغاء الكتم|الغاء كتم)(?:\s|$)([\s\S]*)")
async def unmute_aljoker(event):
    await event.delete()
    if event.is_private:
        replied_user = await event.client.get_entity(event.chat_id)
        if not is_muted(event.chat_id, event.chat_id):
            return await event.edit("**عــذراً .. هـذا الشخص غيــر مكتــوم هنـا**")
        try:
            unmute(event.chat_id, event.chat_id)
            muted_users.remove(replied_user)
        except Exception as e:
            await event.edit(f"**- خطــأ **\n`{e}`")
        else:
            await event.client.send_file(
                event.chat_id,
                joker_unmute,
                caption="**- تـم الغــاء كتــم الشخـص هنـا .. بنجــاح ✓**",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**- الشخـص :** [{replied_user.first_name}](tg://user?id={event.chat_id})\n",
            )
    else:
        user, _ = await get_user_from_event(event)
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
                muted_users.remove(user)
            else:
                result = await event.client.get_permissions(event.chat_id, user.id)
                if result.participant.banned_rights.send_messages:
                    await event.client(
                        EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                    )
        except AttributeError:
            return await edit_or_reply(event, "**- الشخـص غيـر مكـتـوم**")
        except Exception as e:
            return await edit_or_reply(event, f"**- خطــأ : **`{e}`")
        await event.client.send_file(
            event.chat_id,
            joker_unmute,
            caption=f"**- المستخـدم :** {_format.mentionuser(user.first_name, user.id)} \n**- تـم الغـاء كتمـه بنجـاح ✓**",
        )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#الغــاء_الكــتم\n"
                f"**- الشخـص :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**- الدردشــه :** {get_display_name(await event.get_chat())}(`{event.chat_id}`)",
            )
@l313l.ar_cmd(pattern=r"قائمة المكتومين")
async def show_muted_users(event):
    muted_users_str = gvarstatus(muted_users_variable)
    if muted_users_str is None or len(muted_users_str) > 0:
        joker_list = "**᯽︙ قائمة المستخدمين المكتومين:**\n"
        for i, user in enumerate(muted_users, start=1):
            profile_link = f"[{user.first_name}](tg://user?id={user.id})"
            joker_list += f"{i}. {profile_link}\n"
        await event.edit(joker_list)
    else:
        await event.edit("**᯽︙ لا يوجد مستخدمين مكتومين حاليًا**")
# ===================================== # 

@l313l.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "كتم_مؤقت"):
        await event.delete()

#=====================================  #
