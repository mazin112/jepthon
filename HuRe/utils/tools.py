from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditPhotoRequest,
    InviteToChannelRequest,
)
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.types import PeerChannel

from ..core.logger import logging

LOGS = logging.getLogger("super_group")

async def create_supergroup(group_name, client, botusername, descript, photo):
    try:
        result = await client(
            CreateChannelRequest(
                title=group_name,
                about=descript,
                megagroup=True,
            )
        )
        created_chat_idd = result.chats[0].id
        created_idd = result.chats[0]
        LOGS.error(str(created_idd)) 
        created_chat_id = await client.get_entity(PeerChannel(created_chat_idd))
        result = await client(
            ExportChatInviteRequest(
                created_chat_id
            )
        )
        await client(
            InviteToChannelRequest(
                channel=created_chat_id,
                users=[botusername],
            )
        )
        if photo:
            await client(
                EditPhotoRequest(
                    channel=created_chat_id,
                    photo=photo,
                )
            )
    except Exception as e:
        return "error", str(e)
    
    return result, created_chat_id
