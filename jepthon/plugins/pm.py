from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.types import ChatBannedRights
import asyncio
from telethon.sessions import StringSession
import random


# Variable to check if the code is enabled or not
is_protection_enabled = False

# Number of times a user sent messages
user_warnings = {}

# Maximum number of warnings before banning the user
MAX_WARNINGS = 5

# List of image links
IMAGE_LINKS = [
    "https://telegra.ph/file/533ae94032e6eb61f530d.jpg",
    "https://telegra.ph/file/1035a4cc8f4b0b4e5a20a.jpg",
    "https://telegra.ph/file/2bc347111840589a1792e.jpg",
    "https://telegra.ph/file/b1fa56d7aa460caa43464.jpg"
]

# Additional warning messages (including the new warning)
additional_warnings = [
    "مالك الحساب مشغول الآن عندما يصبح متصل سيقوم بالرد عليك.",
    """__حسناً لقد قمت بأبلاغ مالك الحساب عندما يصبح متصلاً بالإنترنت \
أو عندما يكون مالك الحساب متاحاً سوف يقوم بالرد عليك لذلك ارجوك انتظر__\
**لكن في الوقت الحالي لا تكرر ارسال الرسائل  🙁💞**""",
    "لحظياً مالك الحساب مشغول، الرجاء الانتظار وعدم تكرار الرسائل.",
    "اذا ترسل رسالة أخرى سأقوم بحظرك تلقائيًا.",
    "مالك الحساب غير موجود حاليًا، الرجاء الانتظار وعدم تكرار الرسائل.",
    "مالك الحساب يرد على الكل لكن ممكن يتجاهل بعض الأشخاص أحيانًا، اصبر قليلاً.",
    """ههاه لازم تصبر مالك الحساب ما شاف الرسالة انتظر مالك الحساب يرد على الكل بس ما اعرف اذا كان اكو كم شخص يتجاهلهم بس اصبرمالك الحساب راح يرد عليك لما يكون متصل، اذا راد يرد عليك اصلا  🙂🌿""",]
    # Add the new warning here
USER_BOT_WARN_ZERO =    "⌯︙حذࢪتك وكتـلك لا تكࢪࢪ تَم حظࢪك بنجاح ما ٱكدر اخليك تزعج المالك \n- ⌯︙بباي 🙁🤍"

# Function to delete all warning messages from the chat
async def delete_warning_messages(chat_id):
    try:
        # Fetch all warning messages from the chat
        async for message in client.iter_messages(chat_id, from_user="me"):
            if message.text.startswith(("  لحظياً مالك الحساب ", "ههاه", "__حسناً لقد قمت بأبلاغ","   اذا ترسل رسالة ","")):
                # Delete the warning message
                await message.delete()
    except Exception as e:
        print(f"An error occurred while deleting warning messages: {e}")

# Function to block the user and send a random image before banning
async def block_user(event):
    if event.is_private:
        user = await event.get_chat()
    else:
        user = await client.get_entity(event.chat_id)  # Get the user by their ID
        if not user:
            return

    # Send a random image before banning
    random_image_link = random.choice(IMAGE_LINKS)
    await event.respond(f"[{user.first_name}]({random_image_link})\n تم حظره بنجاح، لا يمكنه مراسلتك بعد الآن 🧸♥")

    # Block the user
    await client(BlockRequest(user.id))

# Call the function when receiving the ".بلوك" command
@client.on(events.NewMessage(pattern=r'\.بلوك'))
async def on_block_command(event):
    if not is_protection_enabled:
        await event.respond("يجب تشغيل الحماية أولاً استخدم أمر `.حماية الخاص تشغيل`")
        return

    await block_user(event)
# Function to enable protection
@client.on(events.NewMessage(pattern=r'\.حماية الخاص (تشغيل|ايقاف)'))
async def handle_protection_command(event):
    global is_protection_enabled

    # Get the command from the message text
    command = event.pattern_match.group(1)

    if command == "تشغيل":
        is_protection_enabled = True
        await event.message.edit("تم تفعيل حماية الخاص")
        await asyncio.sleep(1)  # Wait for 5 seconds
        await event.message.delete()  # Delete the message after 5 seconds
    elif command == "ايقاف":
        is_protection_enabled = False
        await event.message.edit("تم إيقاف حماية الخاص")
        await asyncio.sleep(1)  # Wait for 5 seconds
        await event.message.delete()

# Function to handle new messages and send warnings
@client.on(events.NewMessage)
async def handle_new_message(event):
    global is_protection_enabled
    # Check if the code is enabled before continuing
    if not is_protection_enabled:
        return

    # Ignore messages from groups and channels
    if event.is_group or event.is_channel:
        return

    # Get the sender ID
    sender_id = event.sender_id

    # Get the bot's ID
    bot_id = await client.get_me()

    # Check if the sender is the bot itself
    if sender_id == bot_id.id:
        return

    user_id = event.sender_id
    # Check if the user has already been warned before
    if user_id in user_warnings and user_warnings[user_id] >= MAX_WARNINGS:
        try:
            # Delete all previous warning messages sent by the bot
            await delete_warning_messages(event.chat_id)

            # Send the ban message
            await event.reply(USER_BOT_WARN_ZERO)

            # Clear previous warnings
            user_warnings[user_id] = 0

            # Ban the user
            await client(BlockRequest(user_id))
            return
        except Exception as e:
            print(f"An error occurred while banning the user: {e}")
            return

    # User mention for the warning message
    user_entity = await event.get_sender()
    user_mention = user_entity.first_name if user_entity.first_name else user_entity.username

    # Send a random additional warning message
    additional_warning = random.choice(additional_warnings)
    try:
        await event.reply(f"{additional_warning} {user_warnings.get(user_id, 0)}/{MAX_WARNINGS} من التحذيرات لا تكرر حتى ما تنحظر من البوت.")
    except Exception as e:
        print(f"An error occurred while sending the warning message: {e}")

    # Update the user's warning count
    if user_id in user_warnings:
        user_warnings[user_id] += 1
    else:
        user_warnings[user_id] = 1

# Function to handle the ".سماح" command to disable protection
@client.on(events.NewMessage(pattern=r'\.(س|سماح)'))
async def handle_allow_command(event):
    global is_protection_enabled
    if is_protection_enabled:
        is_protection_enabled = False
        # Respond with the allowed message
        try:
            await event.message.edit("تم السماح بإرسال الرسائل")
        except Exception as e:
            print(f"An error occurred while editing the message: {e}")

        # Delete all warning messages
        await delete_warning_messages(event.chat_id)

        # Reset user warnings
        global user_warnings
        user_warnings = {}

