from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid 
import requests
import m3u8
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message    
from p_bar import progress_bar    
from subprocess import getstatusoutput    
from aiohttp import ClientSession    
import helper    
from logger import logging    
import time    
import asyncio    
from pyrogram.types import User, Message    
import sys    
import re    
import os 
import urllib
import urllib.parse
import tgcrypto
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="❤️‍🔥 Devloper",
                url="https://t.me/scammer_botxz",
            ),
            InlineKeyboardButton(
                text="✨ Backup Channel",
                url="https://t.me/scammer_batches",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💫 Updates Channel",
                url="https://t.me/scammer_botxz1",
            ),
            
        ],
    ]
)

photostart = 'https://envs.sh/qMe.jpg'
getstatusoutput(f"wget {photostart} -O 'photostart.jpg'")    
photo_start= "photostart.jpg"

yt_imag = 'https://envs.sh/PQ_.jpg'
getstatusoutput(f"wget {yt_imag} -O 'photo.jpg'")    
yt_image = "photo.jpg"

scammer_captio = 'https://envs.sh/PXK.jpg'
getstatusoutput(f"wget {scammer_captio} -O 'photo2.jpg'")    
scammer_caption = "photo2.jpg"

credit ="😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~" 

OWNER = int(os.environ.get("OWNER", 7326397503))
try: 
    ADMINS=[] 
    for x in (os.environ.get("ADMINS", "7326397503 5702090016").split()):  
        ADMINS.append(int(x)) 
except ValueError: 
        raise Exception("Your Admins list does not contain valid integers.") 
ADMINS.append(OWNER)

bot = Client("bot",    
   bot_token="7412431777:AAFwfsOegtbhdq8FpCqBvQ1UJVs6GtJbYDg",    
   api_id= 21179966,    
   api_hash= "d97919fb0a3c725e8bb2a25bbb37d57c"
)

capt_start = "**👋 ʜᴇʟʟᴏ!\n\n🌟ɪ ᴀᴍ ᴛxᴛ ꜰɪʟᴇ ᴅᴏᴡʟᴏᴀᴅᴇʀ ʙᴏᴛ** \n\n❤️‍🔥 **ᴘʀᴇꜱꜱ /scammer ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʙʏ ᴛxᴛ**\n\n✨ **supported links /links**\n\n❤️‍🩹 **ᴊᴏɪɴ ᴏᴜʀ <a href='https://t.me/scammer_botxz1'>ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ</a>** \n\n💗 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href='https://t.me/Scammer_botxz'>😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~ </a>\n-═════━‧₊˚❀༉‧₊˚.━═════-"

@bot.on_message(filters.command(["start"]))    
async def account_login(bot: Client, m: Message): 
    edit = await m.reply_text('💫')
    time.sleep(3)
    await edit.delete()   
    await bot.send_photo(chat_id=m.chat.id, photo=photo_start, caption=capt_start, reply_markup=keyboard)
    
@bot.on_message(filters.command("Stop")) #& filters.user(ADMINS)) 
async def restart_handler(_, m):  
    await m.reply_text("🚦**STOPPED**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv) 

# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════   
@bot.on_message(filters.command(["scammer"]))    
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚.━═════-')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(OWNER, x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"    
    
    try:    
        with open(x, "r") as f:    
            content = f.read()    
        content = content.split("\n")    
        links = []    
        for i in content:    
            links.append(i.split("://", 1))    
        os.remove(x)    
    except:    
        await m.reply_text("Invalid file input.")    
        os.remove(x)    
        return 
    
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input0: Message = await bot.listen(editable.chat.id)    
    raw_text = input0.text    
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0



    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"  



    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʏᴏᴜʀ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3


    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `ʜᴛᴛᴘꜱ://ɢʀᴀᴘʜ.ᴏʀɢ/ꜰɪʟᴇ/45ꜰ562ᴅᴄ05ʙ2874ᴄ7277ᴇ.ᴊᴘɢ`ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input6 = message = await bot.listen(editable.chat.id)   
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            if "visionias" in url:    
                async with ClientSession() as session:    
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                                         'Accept-Language': 'en-US,en;q=0.9', 
                                                         'Cache-Control': 'no-cache', 
                                                         'Connection': 'keep-alive', 
                                                         'Pragma': 'no-cache', 
                                                         'Referer': 'http://www.visionias.in/', 
                                                         'Sec-Fetch-Dest': 'iframe', 
                                                         'Sec-Fetch-Mode': 'navigate', 
                                                         'Sec-Fetch-Site': 'cross-site', 
                                                         'Upgrade-Insecure-Requests': '1', 
                                                         'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                                                         'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 
                                                         'sec-ch-ua-mobile': '?1', 
                                                         'sec-ch-ua-platform': '"Android"',}) as resp:    
                        text = await resp.text()    
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
                        
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()    
            name = f'{str(count).zfill(3)})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~{name1[:60]}'  
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
  
    
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
  
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
                
            try:
  
                cc = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n **𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                ccyt = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n**Video Link** - {url}\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n **𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'    
                cc1 = f'**[ 📕 ] 𝗣𝗗𝗙 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐏𝐝𝐟 𝐓𝐢𝐭𝐥𝐞** : {name1} **😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.pdf \n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'    
                if "drive" in url:    
                    try:    
                        ka = await helper.download(url, name)    
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)    
                        count+=1    
                        os.remove(ka)    
                        time.sleep(1)    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(e.x)    
                        continue  

                elif ".pdf" in url:
                    
                    try:    
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'    
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"    
                        os.system(download_cmd)    
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', thumb=scammer_caption, caption=cc1)    
                        count +=1
                        os.remove(f'{name}.pdf')    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(2)    
                        continue
                    
                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=yt_image, caption=ccyt)
                        count +=1
                    except Exception as e:
                        await m.reply_text(str(e))    
                        await asyncio.sleep(3)   
                        continue
                         
                          
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"    
                    prog = await m.reply_text(Show)    
                    res_file = await helper.download_video(url, cmd, name)    
                    filename = res_file    
                    await prog.delete(True)    
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    count += 1    
                    time.sleep(1)
                    
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n{str(e)}\n**Name** - {name}\n\n═════━‧₊˚❀༉‧₊˚.━═════"
                )
                continue
                
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done Boss✨")
    
# ═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════        
@bot.on_message(filters.command(["cw"]) & filters.user(ADMINS))    
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ `cw` ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚.━═════-')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(OWNER, x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"    
    
    try:    
        with open(x, "r") as f:    
            content = f.read()    
        content = content.split("\n")    
        links = []    
        for i in content:    
            links.append(i.split("://", 1))    
        os.remove(x)    
    except:    
        await m.reply_text("Invalid file input.")    
        os.remove(x)    
        return 
    
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input0: Message = await bot.listen(editable.chat.id)    
    raw_text = input0.text    
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0



    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"  



    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʏᴏᴜʀ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3


    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `ʜᴛᴛᴘꜱ://ɢʀᴀᴘʜ.ᴏʀɢ/ꜰɪʟᴇ/45ꜰ562ᴅᴄ05ʙ2874ᴄ7277ᴇ.ᴊᴘɢ`ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input6 = message = await bot.listen(editable.chat.id)   
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            
            if "edge.api.brightcove.com" in url:
                bcov = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            elif 'youtu' in url:
                url = url
                
            elif ".pdf" in url:
                url = url.replace(" ","%20")
                        
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()    
            name = f'{str(count).zfill(3)})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~{name1[:60]}'  
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
  
    
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
  
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
                
            try:
  
                cc = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                ccyt = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n**Video Link** - {url}\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'    
                cc1 = f'**[ 📕 ] 𝗣𝗗𝗙 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐏𝐝𝐟 𝐓𝐢𝐭𝐥𝐞** : {name1} **😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.pdf \n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'    
                if "drive" in url:    
                    try:    
                        ka = await helper.download(url, name)    
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)    
                        count+=1    
                        os.remove(ka)    
                        time.sleep(1)    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(e.x)    
                        continue  

                elif ".pdf" in url:
                    
                    try:    
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'    
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"    
                        os.system(download_cmd)    
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', thumb=scammer_caption, caption=cc1)    
                        count +=1
                        os.remove(f'{name}.pdf')    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(2)    
                        continue
                    
                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=yt_image, caption=ccyt)
                        count +=1
                    except Exception as e:
                        await m.reply_text(str(e))    
                        await asyncio.sleep(3)   
                        continue
                         
                          
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"    
                    prog = await m.reply_text(Show)    
                    res_file = await helper.download_video(url, cmd, name)    
                    filename = res_file    
                    await prog.delete(True)    
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    count += 1    
                    time.sleep(1)
                    
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n═════━‧₊˚❀༉‧₊˚.━═════"
                )
                continue
                
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done Boss✨")

# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
@bot.on_message(filters.command(["pw"]) & filters.user(ADMINS))
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ `pw` ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚.━═════-')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(OWNER, x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"    
    
    try:    
        with open(x, "r") as f:    
            content = f.read()    
        content = content.split("\n")    
        links = []    
        for i in content:    
            links.append(i.split("://", 1))    
        os.remove(x)    
    except:    
        await m.reply_text("Invalid file input.")    
        os.remove(x)    
        return 
    
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input0: Message = await bot.listen(editable.chat.id)    
    raw_text = input0.text    
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0



    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"  



    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʏᴏᴜʀ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3


    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `ʜᴛᴛᴘꜱ://ɢʀᴀᴘʜ.ᴏʀɢ/ꜰɪʟᴇ/45ꜰ562ᴅᴄ05ʙ2874ᴄ7277ᴇ.ᴊᴘɢ`ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input6 = message = await bot.listen(editable.chat.id)   
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            
            if 'd26g5bnklkwsh4.cloudfront.net' in url or 'd1d34p8vz63oiq.cloudfront.net' in url or "master.mpd" in url:
                id =  url.split("/")[-2] 
                token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzE4MzEzMTEuNTg4LCJkYXRhIjp7Il9pZCI6IjYyYTYwYWM0MWEzMDk3MDAxMTMyMmZjOCIsInVzZXJuYW1lIjoiODI3MjA1NTA1NCIsImZpcnN0TmFtZSI6IlVOSVFVRSIsImxhc3ROYW1lIjoiVU5JUVVFIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sImVtYWlsIjoibXVqZWVtMDAwQGdtYWlsLmNvbSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTczMTIyNjUxMX0.n_9ZmxTgNoX57Pns8FekvZ9DtbGOsDPYoor3NHzLqcA' 
                url = 'https://pwapi-aaebd595f347.herokuapp.com/'+ id +'/master.m3u8?token='+ token
                
            elif 'youtu' in url:
                url = url
                        
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()    
            name = f'{str(count).zfill(3)})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~{name1[:60]}'  
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
  
    
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
  
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
                
            try:
  
                cc = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                ccyt = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n**Video Link** - {url}\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'    
                cc1 = f'**[ 📕 ] 𝗣𝗗𝗙 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐏𝐝𝐟 𝐓𝐢𝐭𝐥𝐞** : {name1} **😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.pdf \n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'    
                if "drive" in url:    
                    try:    
                        ka = await helper.download(url, name)    
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)    
                        count+=1    
                        os.remove(ka)    
                        time.sleep(1)    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(e.x)    
                        continue  

                elif ".pdf" in url:
                    
                    try:    
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'    
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"    
                        os.system(download_cmd)    
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', thumb=scammer_caption, caption=cc1)    
                        count +=1
                        os.remove(f'{name}.pdf')    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(2)    
                        continue
                    
                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=yt_image, caption=ccyt)
                        count +=1
                    except Exception as e:
                        await m.reply_text(str(e))    
                        await asyncio.sleep(3)   
                        continue
                         
                          
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"    
                    prog = await m.reply_text(Show)    
                    res_file = await helper.download_video(url, cmd, name)    
                    filename = res_file    
                    await prog.delete(True)    
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    count += 1    
                    time.sleep(1)
                    
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n═════━‧₊˚❀༉‧₊˚.━═════"
                )
                continue
                
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done Boss✨")

# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════       
@bot.on_message(filters.command(["ut"]) & filters.user(ADMINS))
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ `ut` ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚.━═════-')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(OWNER, x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"    
    
    try:    
        with open(x, "r") as f:    
            content = f.read()    
        content = content.split("\n")    
        links = []    
        for i in content:    
            links.append(i.split("://", 1))    
        os.remove(x)    
    except:    
        await m.reply_text("Invalid file input.")    
        os.remove(x)    
        return 
    
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input0: Message = await bot.listen(editable.chat.id)    
    raw_text = input0.text    
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0



    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"  



    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʏᴏᴜʀ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3


    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `ʜᴛᴛᴘꜱ://ɢʀᴀᴘʜ.ᴏʀɢ/ꜰɪʟᴇ/45ꜰ562ᴅᴄ05ʙ2874ᴄ7277ᴇ.ᴊᴘɢ`ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input6 = message = await bot.listen(editable.chat.id)   
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            
            if "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)
                    
                else:
                    url = url     
                
            elif 'youtu' in url:
                url = url
                        
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()    
            name = f'{str(count).zfill(3)})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~{name1[:60]}'  
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
  
    
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
  
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
                
            try:
  
                cc = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                ccyt = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n**Video Link** - {url}\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'    
                cc1 = f'**[ 📕 ] 𝗣𝗗𝗙 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐏𝐝𝐟 𝐓𝐢𝐭𝐥𝐞** : {name1} **😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.pdf \n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'    
                if "drive" in url:    
                    try:    
                        ka = await helper.download(url, name)    
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)    
                        count+=1    
                        os.remove(ka)    
                        time.sleep(1)    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(e.x)    
                        continue  

                elif ".pdf" in url:
                    
                    try:    
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'    
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"    
                        os.system(download_cmd)    
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', thumb=scammer_caption, caption=cc1)    
                        count +=1
                        os.remove(f'{name}.pdf')    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(2)    
                        continue
                    
                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=yt_image, caption=ccyt)
                        count +=1
                    except Exception as e:
                        await m.reply_text(str(e))    
                        await asyncio.sleep(3)   
                        continue
                         
                          
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"    
                    prog = await m.reply_text(Show)    
                    res_file = await helper.download_video(url, cmd, name)    
                    filename = res_file    
                    await prog.delete(True)    
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    count += 1    
                    time.sleep(1)
                    
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n═════━‧₊˚❀༉‧₊˚.━═════"
                )
                continue
                
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done Boss✨")
        
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════       
@bot.on_message(filters.command(["kgs"]) & filters.user(ADMINS))
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ `kgs` ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚.━═════-')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(OWNER, x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"    
    
    try:    
        with open(x, "r") as f:    
            content = f.read()    
        content = content.split("\n")    
        links = []    
        for i in content:    
            links.append(i.split("://", 1))    
        os.remove(x)    
    except:    
        await m.reply_text("Invalid file input.")    
        os.remove(x)    
        return 
    
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input0: Message = await bot.listen(editable.chat.id)    
    raw_text = input0.text    
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0



    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"  



    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʏᴏᴜʀ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3


    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `ʜᴛᴛᴘꜱ://ɢʀᴀᴘʜ.ᴏʀɢ/ꜰɪʟᴇ/45ꜰ562ᴅᴄ05ʙ2874ᴄ7277ᴇ.ᴊᴘɢ`ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input6 = message = await bot.listen(editable.chat.id)   
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            
            if '.pdf' in url:
                url = url.replace(" ","%20")
                
            elif 'kgs-v1.akamaized.net' in url:
                url = url.replace(url.split("/")[-1], raw_text2+".m3u8")
                
            elif "/khansirvod4" in url:
              url = url.replace(url.split("/")[-1], raw_text2+".m3u8")
              
            elif "kgs-v3.akamaized.net" in url:
                if raw_text2 == 360:
                   url = url.replace('.m3u8', "_360p878kbs/index.m3u8")
                elif raw_text2 == 240:
                   url = url.replace('.m3u8', "_240p264kbs/index.m3u8")
                elif raw_text2 == 144:
                    url = url.replace('.m3u8', "_144p190kbs/index.m3u8")
                elif raw_text2== 720:
                    url = url.replace('.m3u8', "_720p2628kbs/index.m3u8")
                elif raw_text2 == 1080:
                    url = url.replace('.m3u8', "_720p2628kbs/index.m3u8")
                elif raw_text2 == 480:
                    url = url.replace('.m3u8', "_360p878kbs/index.m3u8")
                
            elif 'youtu' in url:
                url = url
                        
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()    
            name = f'{str(count).zfill(3)})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~{name1[:60]}'  
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
  
    
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
  
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
                
            try:
  
                cc = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                ccyt = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n**Video Link** - {url}\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'    
                cc1 = f'**[ 📕 ] 𝗣𝗗𝗙 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐏𝐝𝐟 𝐓𝐢𝐭𝐥𝐞** : {name1} **😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.pdf \n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'    
                if "drive" in url:    
                    try:    
                        ka = await helper.download(url, name)    
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)    
                        count+=1    
                        os.remove(ka)    
                        time.sleep(1)    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(e.x)    
                        continue  

                elif ".pdf" in url:
                    
                    try:    
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'    
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"    
                        os.system(download_cmd)    
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', thumb=scammer_caption, caption=cc1)    
                        count +=1
                        os.remove(f'{name}.pdf')    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(2)    
                        continue
                    
                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=yt_image, caption=ccyt)
                        count +=1
                    except Exception as e:
                        await m.reply_text(str(e))    
                        await asyncio.sleep(3)   
                        continue
                         
                          
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"    
                    prog = await m.reply_text(Show)    
                    res_file = await helper.download_video(url, cmd, name)    
                    filename = res_file    
                    await prog.delete(True)    
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    count += 1    
                    time.sleep(1)
                    
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n═════━‧₊˚❀༉‧₊˚.━═════"
                )
                continue
                
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done Boss✨")
        
# ══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════       
@bot.on_message(filters.command(["cp"]) & filters.user(ADMINS))
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ `kgs` ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚.━═════-')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(OWNER, x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"    
    
    try:    
        with open(x, "r") as f:    
            content = f.read()    
        content = content.split("\n")    
        links = []    
        for i in content:    
            links.append(i.split("://", 1))    
        os.remove(x)    
    except:    
        await m.reply_text("Invalid file input.")    
        os.remove(x)    
        return 
    
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input0: Message = await bot.listen(editable.chat.id)    
    raw_text = input0.text    
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0



    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"  



    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʏᴏᴜʀ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3


    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `ʜᴛᴛᴘꜱ://ɢʀᴀᴘʜ.ᴏʀɢ/ꜰɪʟᴇ/45ꜰ562ᴅᴄ05ʙ2874ᴄ7277ᴇ.ᴊᴘɢ`ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input6 = message = await bot.listen(editable.chat.id)   
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            if 'media-cdn.classplusapp.com' in url:
                tokencp ='eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NDcwOTYwODIsIm9yZ0lkIjozNTExODAsInR5cGUiOjEsIm1vYmlsZSI6IjkxODAwNDQ1ODkwNCIsIm5hbWUiOiJzdWppdCB0aXdhcmkiLCJlbWFpbCI6InN1aml0dGl3YXJpMjIxMzA4QGdtYWlsLmM5bSIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5Ijp0cnVlLCJvcmdDb2RlIjoiYnZqaGkiLCJpc0RpeVN1YmFkbWluIjowLCJmaW5nZXJwcmludElkIjoiMmIzMDFjMzRiODkxZmJhMmE1Y2YyYjYyNDA3NjVhNDIiLCJpYXQiOjE3MjQzMzEwNzcsImV4cCI6MTcyNDkzNTg3N30.0oi58SRgPcKtA-vSoYFBiBh2_dIsGnFnlTak1oaxXZZtAzpEo1omoE5zoc4cim9U'
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': tokencp}).json()['url']

            elif 'videos.classplusapp' in url:
                tokencp ='eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NDcwOTYwODIsIm9yZ0lkIjozNTExODAsInR5cGUiOjEsIm1vYmlsZSI6IjkxODAwNDQ1ODkwNCIsIm5hbWUiOiJzdWppdCB0aXdhcmkiLCJlbWFpbCI6InN1aml0dGl3YXJpMjIxMzA4QGdtYWlsLmM5bSIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5Ijp0cnVlLCJvcmdDb2RlIjoiYnZqaGkiLCJpc0RpeVN1YmFkbWluIjowLCJmaW5nZXJwcmludElkIjoiMmIzMDFjMzRiODkxZmJhMmE1Y2YyYjYyNDA3NjVhNDIiLCJpYXQiOjE3MjQzMzEwNzcsImV4cCI6MTcyNDkzNTg3N30.0oi58SRgPcKtA-vSoYFBiBh2_dIsGnFnlTak1oaxXZZtAzpEo1omoE5zoc4cim9U'
                url1 = url.replace('videos.classplusapp.com', 'media-cdn.classplusapp.com/alisg-cdn-a.classplusapp.com')
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url1}', headers={'x-access-token': tokencp}).json()['url']
            
            elif 'tencdn.classplusapp.com' in url:
                tokencp = 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NDcwOTYwODIsIm9yZ0lkIjozNTExODAsInR5cGUiOjEsIm1vYmlsZSI6IjkxODAwNDQ1ODkwNCIsIm5hbWUiOiJzdWppdCB0aXdhcmkiLCJlbWFpbCI6InN1aml0dGl3YXJpMjIxMzA4QGdtYWlsLmM5bSIsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiY291bnRyeUlTTyI6IjkxIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImlzRGl5Ijp0cnVlLCJvcmdDb2RlIjoiYnZqaGkiLCJpc0RpeVN1YmFkbWluIjowLCJmaW5nZXJwcmludElkIjoiMmIzMDFjMzRiODkxZmJhMmE1Y2YyYjYyNDA3NjVhNDIiLCJpYXQiOjE3MjQzMzEwNzcsImV4cCI6MTcyNDkzNTg3N30.0oi58SRgPcKtA-vSoYFBiBh2_dIsGnFnlTak1oaxXZZtAzpEo1omoE5zoc4cim9U'
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'Host': 'api.classplusapp.com', 'x-access-token': tokencp, 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip',}).json()['url']            
                
            elif 'youtu' in url:
                url = url
                        
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()    
            name = f'{str(count).zfill(3)})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~{name1[:60]}'  
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
  
    
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
  
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
                
            try:
  
                cc = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                ccyt = f'**[ 🎬 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res})😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.mp4\n**Video Link** - {url}\n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'    
                cc1 = f'**[ 📕 ] 𝗣𝗗𝗙 𝗜𝗗 : {str(count).zfill(3)}**\n**𝐏𝐝𝐟 𝐓𝐢𝐭𝐥𝐞** : {name1} **😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~**.pdf \n\n**𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** : **{b_name}** \n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'    
                if "drive" in url:    
                    try:    
                        ka = await helper.download(url, name)    
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)    
                        count+=1    
                        os.remove(ka)    
                        time.sleep(1)    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(e.x)    
                        continue  

                elif ".pdf" in url:
                    
                    try:    
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'    
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"    
                        os.system(download_cmd)    
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', thumb=scammer_caption, caption=cc1)    
                        count +=1
                        os.remove(f'{name}.pdf')    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(2)    
                        continue
                    
                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=yt_image, caption=ccyt)
                        count +=1
                    except Exception as e:
                        await m.reply_text(str(e))    
                        await asyncio.sleep(3)   
                        continue
                         
                          
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"    
                    prog = await m.reply_text(Show)    
                    res_file = await helper.download_video(url, cmd, name)    
                    filename = res_file    
                    await prog.delete(True)    
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    count += 1    
                    time.sleep(1)
                    
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed [😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™]**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n═════━‧₊˚❀༉‧₊˚.━═════"
                )
                continue
                
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done Boss✨")
        
bot.run()