from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.sync import events
from HuRe import l313l

@l313l.on(events.NewMessage(pattern='انضموا'))
async def handle_new_message(event):
    if event.message.sender_id == (await l313l.get_me()).id:
        return
    group_link = event.message.text
    message = f"Join this group/channel: {group_link}"
    await l313l.send_message('username_or_chat_id', message)

@l313l.on(events.NewMessage)
    async def handle_reply(event):
        if event.message.sender_id == (await l313l.get_me()).id:
            return

        if event.message.reply_to_msg_id is not None:
            original_message = await event.message.get_reply_message()
            if original_message.text == message:
                reply_link = event.message.text
                result = await l313l(ImportChatInviteRequest(reply_link))
                print('Joined successfully:', result.chats)

