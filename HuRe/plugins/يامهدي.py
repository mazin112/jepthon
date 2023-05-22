from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.sync import events
from HuRe import l313l

@l313l.on(events.NewMessage(pattern='انضموا'))
async def Hussein(event):
    if event.message.sender_id == l313l.get_me().id:
        return
    group_link = event.message.text
    message = f"انضم لهذه المجموعة/القناة: {group_link}"
    await l313l.send_message('معرف القناة او الايدي', message)
@l313l.on(events.NewMessage)
async def Hussein(event):
    if event.message.sender_id == l313l.get_me().id:
        return
    if event.message.reply_to_msg_id is not None:
        original_message = await event.message.get_reply_message()
        if original_message.text == message:
            reply_link = event.message.text
            result = await l313l(ImportChatInviteRequest(reply_link))
            print('Joined successfully:', result.chats)
