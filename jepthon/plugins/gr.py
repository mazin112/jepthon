from telethon import TelegramClient, events, utils
import asyncio
from telethon.sessions import StringSession
from telethon.tl.types import InputMessagesFilterEmpty
import random



# Start the client
async def main():
    try:
        await client.start()
        print("Client is ready.")
    except Exception as e:
        print(f"Failed to start the client: {e}")
        return

protection_enabled = False

IMAGE_LINKS = [
    "https://telegra.ph/file/533ae94032e6eb61f530d.jpg",
    "https://telegra.ph/file/1035a4cc8f4b0b4e5a20a.jpg",
    "https://telegra.ph/file/2bc347111840589a1792e.jpg",
    "https://telegra.ph/file/b1fa56d7aa460caa43464.jpg"
]

# Define the get_user_from_event function
async def get_user_from_event(event):
    user = None
    if event.reply_to_msg_id:
        # If the command is used by replying to a message, get the replied user
        replied_msg = await event.get_reply_message()
        if replied_msg.sender_id:
            user = await event.client.get_entity(replied_msg.sender_id)
    else:
        # If the command has a username provided, get the user based on the username
        input_str = event.pattern_match.group(1)
        if input_str:
            user = await event.client.get_entity(input_str)

    return user

# Define the edit_delete and edit_or_reply functions
async def edit_delete(event, text):
    await event.edit(text)
    await asyncio.sleep(3)
    await event.delete()

# Add a global variable to store the user ID of the client
user_id = None

# Define a function to get the user ID of the client
async def get_user_id():
    global user_id
    if user_id is None:
        me = await client.get_me()
        user_id = me.id
    return user_id

# Modify the edit_or_reply function to check if the sender is the user running the code
async def edit_or_reply(event, text):
    if event.sender_id == await get_user_id():
        return await event.respond(text)
    else:
        return await event.edit(text)
        
@client.on(events.NewMessage(pattern=r'\.حماية المجموعة ايقاف'))
async def handle_disable_protection(event):
    global protection_enabled
    if event.is_group:
        protection_enabled = False
        await edit_or_reply(event, "✅ تم إيقاف حماية المجموعة.")
    else:
        await edit_or_reply(event, "⚠️ هذه ليست مجموعة.")

# Modify the endmute function to check if protection is enabled before executing the command
async def endmute(event, user_identifier=None):
    "لـطرد شـخض من الـكروب"
    if not protection_enabled:
        return await edit_or_reply(event, "⚠️ يرجى تفعيل حماية المجموعة بأمر .حماية المجموعة تشغيل")

    # If no user identifier is provided, check if the command is used as a reply
    if not user_identifier:
        if event.is_reply:
            replied_msg = await event.get_reply_message()
            if replied_msg.sender:
                user_identifier = replied_msg.sender.id
            else:
                return await edit_or_reply(event, "⚠️ لم يتم العثور على المستخدم المقصود.")
        else:
            return await edit_or_reply(event, "⚠️ يرجى تحديد مستخدم للطرد.")
    
    try:
        # Convert the user identifier to an integer to use it as a user ID
        user_id = int(user_identifier)
        user = await event.client.get_entity(user_id)
    except ValueError:
        return await edit_or_reply(event, f"⚠️ يجب تحديد معرّف المستخدم الصحيح (user ID).")
    except Exception as e:
        return await edit_or_reply(event, f"⚠️ لم يتم العثور على المستخدم بسبب خطأ: {str(e)}")

    if not user:
        return await edit_or_reply(event, "⚠️ لم يتم العثور على المستخدم.")

    if user.id == (await event.client.get_me()).id:
        return await edit_delete(event, "⚠️ لا يمكنك طرد نفسك.")
    # Select a random image from the provided links
    random_image = random.choice(IMAGE_LINKS)
    caption = "✅ تم طرد المستخدم بنجاح."

    catevent = await event.client.send_file(
        event.chat_id,
        random_image,
        caption=caption,
        reply_to=event.message.id
    )

    try:
        await event.client.kick_participant(event.chat_id, user.id)
    except Exception as e:
        await catevent.edit(f"⚠️ لم يتم طرد المستخدم بسبب خطأ: {str(e)}")
    else:
        # Edit the message with the success image after kicking the user
        await asyncio.sleep(1)
        await catevent.edit(f"⚠️ المستخدم [{user.first_name}](tg://user?id={user.id})\n {caption}")
        # Delete all messages of the kicked user from the group
        deleted_message_ids = await delete_user_messages(event.client, event.chat_id, user.id)
        print(f"Deleted messages: {deleted_message_ids}")

# Modify the endban function to check if the sender is the user running the code
# Inside endban function
async def endban(event, user_identifier=None):
    "لـحـظـر شـخـص مـع حـذف رسـائلـه"
    if not protection_enabled:
        return await edit_or_reply(event, "⚠️ يرجى تفعيل حماية المجموعة بأمر .حماية المجموعة تشغيل")

    # If no user identifier is provided, check if the command is used as a reply
    if not user_identifier:
        if event.is_reply:
            replied_msg = await event.get_reply_message()
            if replied_msg.sender:
                user_identifier = replied_msg.sender.id
            else:
                return await edit_or_reply(event, "⚠️ لم يتم العثور على المستخدم المقصود.")
        else:
            return await edit_or_reply(event, "⚠️ يرجى تحديد مستخدم للحظر.")
    
    try:
        # Convert the user identifier to an integer to use it as a user ID
        user_id = int(user_identifier)
        user = await event.client.get_entity(user_id)
    except ValueError:
        return await edit_or_reply(event, f"⚠️ يجب تحديد معرّف المستخدم الصحيح (user ID).")
    except Exception as e:
        return await edit_or_reply(event, f"⚠️ لم يتم العثور على المستخدم بسبب خطأ: {str(e)}")

    if not user:
        return await edit_or_reply(event, "⚠️ لم يتم العثور على المستخدم.")

    if user.id == (await event.client.get_me()).id:
        return await edit_delete(event, "⚠️ لا يمكنك حظر نفسك.")

    # Select a random image from the provided links
    random_image = random.choice(IMAGE_LINKS)
    caption = "🚫 تم حظر المستخدم بنجاح."

    catevent = await event.client.send_file(
        event.chat_id,
        random_image,
        caption=caption,
        reply_to=event.message.id
    )

    try:
        await event.client.edit_permissions(event.chat_id, user.id, view_messages=False)
    except Exception as e:
        await catevent.edit(f"⚠️ لم يتم حظر المستخدم بسبب خطأ: {str(e)}")
    else:
        # Edit the message with the success image after banning the user
        await asyncio.sleep(1)
        await catevent.edit(f"⚠️ المستخدم [{user.first_name}](tg://user?id={user.id})\n {caption}")
        # Delete all messages of the banned user from the group
        deleted_message_ids = await delete_user_messages(event.client, event.chat_id, user.id)
        print(f"Deleted messages: {deleted_message_ids}")

# Modify the endunban function to check if the sender is the user running the code
async def endunban(event, user_username=None):
    "لـإلـغاء حـظـر شـخـص والسماح له بالانضمام إلى المجموعة مرة أخرى"
    if not protection_enabled:
        return await edit_or_reply(event, "⚠️ يرجى تفعيل حماية المجموعة بأمر .حماية المجموعة تشغيل")

    if not user_username:
        # If no username is provided, check if the command is used as a reply
        if event.is_reply:
            replied_msg = await event.get_reply_message()
            if replied_msg.sender:
                user_username = replied_msg.sender.username
            else:
                return await edit_or_reply(event, "⚠️ لم يتم العثور على المستخدم المقصود.")
        else:
            return await edit_or_reply(event, "⚠️ يرجى تحديد مستخدم لإلغاء الحظر.")

    try:
        user = await event.client.get_entity(user_username)
    except ValueError:
        return await edit_or_reply(event, f"⚠️ لم يتم العثور على المستخدم: {user_username}")

    # Unban the user
    try:
        await event.client.edit_permissions(event.chat_id, user.id, view_messages=True)
    except Exception as e:
        await edit_or_reply(event, f"⚠️ لم يتم إلغاء حظر المستخدم بسبب خطأ: {str(e)}")
    else:
        await edit_or_reply(event, f"✅ تم إلغاء حظر المستخدم [{user.first_name}](tg://user?id={user.id})")
    await asyncio.sleep(1)  # Wait for 1 second
    await event.message.delete()

# Define the delete_user_messages function
async def delete_user_messages(client, chat_id, user_id):
    deleted_message_ids = []
    async for message in client.iter_messages(chat_id, from_user=user_id):
        try:
            await client.delete_messages(chat_id, message)
            deleted_message_ids.append(message.id)
        except Exception as e:
            print(f"Error deleting message {message.id}: {str(e)}")
    return deleted_message_ids

# Define a function to get the group username based on the group ID
async def get_group_username(group_id):
    try:
        entity = await client.get_entity(group_id)
        return entity.username
    except Exception as e:
        print(f"Failed to get group username: {e}")
        return None

@client.on(events.NewMessage(pattern=r'\.حماية المجموعة تشغيل'))
async def handle_enable_protection(event):
    global protection_enabled, group_id
    if event.is_group:
        group_id = event.chat_id
        group_username = await get_group_username(group_id)
        if group_username:
            protection_enabled = True
            await edit_or_reply(event, "✅ تم تفعيل حماية المجموعة.")
        else:
            await edit_or_reply(event, "⚠️ هذه ليست مجموعة.")
    else:
        await edit_or_reply(event, "⚠️ هذه ليست مجموعة.")

@client.on(events.NewMessage(pattern=r'\.طرد(\s+@\w+)?'))
async def handle_endmute(event):
    user_username = event.pattern_match.group(1) if event.pattern_match.group(1) else None
    await endmute(event, user_username)

@client.on(events.NewMessage(pattern=r'\.حظر(\s+@\w+)?'))
async def handle_endban(event):
    user_username = event.pattern_match.group(1) if event.pattern_match.group(1) else None
    await endban(event, user_username)

@client.on(events.NewMessage(pattern=r'\.الغاء الحظر(\s+@\w+)?'))
async def handle_endunban(event):
    user_username = event.pattern_match.group(1) if event.pattern_match.group(1) else None
    await endunban(event, user_username)

# 
