#import
import discord
from  dotenv import load_dotenv
import os
from discord.ext import commands
import time
import schedule

# .env
load_dotenv()

# discord
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

# start server
@bot.event
async def on_ready():
    print(f">>> {bot.user} is ready <<<")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("I am NUN not SUS!"))

# slash-ping
@bot.command(description="確認機器人在線狀況")
async def ping(ctx): 
    await ctx.respond(f"Pong! 我還在線喔！")

# slash-clear
@commands.has_permissions(administrator=True)
@bot.command(description="清理頻道")
async def clear(ctx, num: int):
    await ctx.respond("ok!")
    await ctx.channel.purge(limit=num + 1)

# NUN 匿名聊天
@bot.event
async def on_message(message):
    if message.channel.type == discord.ChannelType.private:
        channel = bot.get_channel(1051043085666242610)
        msg = message.content
        tl = time.localtime(time.time())
        new_time = "%4s.%2s.%2s %2s'%2s" % (
            str(tl.tm_year), str(tl.tm_mon), str(tl.tm_mday), str(tl.tm_hour), str(tl.tm_min))
        title = "nick-" + str(new_time)
        await channel.create_thread(name=title, content=str(msg))


bot.run(os.getenv('TOKEN'))
