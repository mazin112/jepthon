
#Reda
import asyncio 
import shutil
import requests
from requests.exceptions import JSONDecodeError
import json
import os
import re
from bs4 import BeautifulSoup as bs
import time
from datetime import timedelta
import math
import base64
from HuRe import l313l 
#from ..Config import Config
#By Reda
@l313l.ar_cmd(func=lambda m:'reda')
async def tiktok_dl(message):
    ms = message.text
    if message.sender.id == Config.OWNER_ID or message.sender.id in Config.SUDO_USERS:
            if ms.startswith(".تك") and ("https://tiktok.com/" in ms or "https://vm.tiktok.com/" in ms):
                await message.delete()
                a = await l313l.send_message(message.chat.id, 'يجري البحث عن الملف..')
                link = re.findall(r'\bhttps?://.*[(tiktok|douyin)]\S+', message.text)[0]

                try:
                    response = requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={link}&key=godownloader.com")
                    data = response.json()
                    video_link = data["video_no_watermark"]
                    response = requests.get(video_link)
                    video_data = response.content
                    directory = str(round(time.time()))
                    filename = str(int(time.time()))+'.mp4'
                    os.mkdir(directory)
                    video_filename = f"{directory}/{filename}"
                    with open(video_filename, "wb") as file:
                        file.write(video_data)
                
                except JSONDecodeError:
                    return await a.edit("الرابط غير صحيح تأكد منه!")
                except Exception as er:
                    return await a.edit(f"حدث خطأ قم بتوجيه الرسالة الى مطوري @rd0r0\n{er}")
            
            
                
                await a.edit(f' يجري التحميل للخادم..!\n'
                   f' يجري الرفع للتلجرام⏳__')
                start = time.time()
                title = "فيديو"
                filesize_bytes = os.path.getsize(video_filename)
                filesize = filesize_bytes / (1024 * 1024)
                catid = await reply_id(message)
                await message.client.send_file(
                   message.chat_id, f"./.   {directory}/{filename}", reply_to=catid,     force_document=True, parse_mode='md',     caption=f"**الملف : ** {filename}\n**الحجم :**     {filesize} MB"
                 )
        
                await a.delete()
     
                shutil.rmtree(directory)
    #else:
       # return None
