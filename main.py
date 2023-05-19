import discord
from  dotenv import load_dotenv
import os

# .env
load_dotenv()
bot = discord.Bot()

@bot.event  # print "bot is ready"
async def on_ready():
    print(f">>> {bot.user} is ready <<<")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("I am NUN not SUS!"))

@bot.command(description="Ping / Pong!")
async def ping(ctx): 
    await ctx.respond(f"Pong! 我還在線喔！")



bot.run(os.getenv('TOKEN'))