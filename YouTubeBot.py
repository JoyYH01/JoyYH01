import requests,telebot,shutil
from pytube import YouTube
from pytube import exceptions
from pytube import Playlist
from shutil import *
from telethon import TelegramClient,events

client = TelegramClient("bot", 24694743, "f81bb69a0d9ac25aa7d029f2464a56d8")

client.start()
print("Bot Running")
@client.on(events.NewMessage(pattern="^/start$"))

async def start(event):
    await event.reply("طريقه التحميل سهله غير كلمه url برابط الفيديو اللي عايز تحمله سواء كنت عايز تحمله فيديو عادي او اغنيه \n\n/mp3 url لو عايز تنزل اغنيه\n/mp4 url لو عايز تنزل فيديو \n\nلو عايز تحمل قائمه تشغيل كامله بدوسه واحده فمش هتعرف تحملها من البوت لكن هتعرف تحملها من اسكربت البايثون بتاعنا 😀 ابعت /py عشان ابعتلك الاسكربت والشرح \n\nالمطور: @YassaHany\nقناة المطور: @YassaTeam\n")


@client.on(events.NewMessage(pattern="^/py"))

async def start(event):
    
    url=(event.text)
    url=url.split()[1:]
    url=" ".join(map(str,url))
    print(url)
    
    await event.reply("https://t.me/YassaTeam/5513")


@client.on(events.NewMessage(pattern="^/mp3"))

async def start(event):
    
    url=(event.text)
    url=url.split()[1:]
    url=" ".join(map(str,url))
    print(url)
    #url="https://youtu.be/Cmpk8NKhegI"
    try:
            yt = YouTube(url)
    except exceptions.ExtractError:
        await event.reply("الرابط غلط او انت مكتبتش رابط اصلا.. اكتبه صح وبطل فزلكه 🙄")
    except exceptions.VideoUnavailable:
        await event.reply("الفيديو دا غير متاح او اتحذف يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲")
    except exceptions.VideoPrivate:
            await event.reply("الفيديو دا برايفت يحب يعني مش هعرف احملهولك جرب غيرو كدا 🥲")
    except exceptions.VideoRegionBlocked:
              await event.reply("الفيديو دا اتعمله بلوك من يوتيوب يحب يعني مش هعرف احملهولك جرب غيرو كدا🥲")
              
    else:
        await event.reply("تمام يحب بيتم تحميل اللي طلبته حاليا..انتظر 🤍")
        chc = yt.streams.get_audio_only().download("Bot")
        nam = chc.splitlines()[0].replace(".mp4", "")
        nam = nam.splitlines()[0].replace(".webm", "")
        nam=shutil.move(chc,""+nam+".mp3")
        print(nam)
        try:
            await client.send_file(event.chat.id, nam,caption="حملتهولك اهو اي خدعه ابسط اعم 🌚🤍\n ومتنساش تشترك ف قناتي ماشي 🌚👍 \n @YassaTeam")
            rmtree("Bot")
        except:
            await event.reply("الملف كبير مش هقدر احمله وابعتهولك")
        else:
            print("er")







client.run_until_disconnected()
