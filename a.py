import discord
from discord.ext import commands

# 設定機器人的指令前綴符號

# 建立機器人客戶端
bot = commands.Bot()

# 定義清空指定頻道訊息的指令
@bot.command()
async def clear(ctx, channel_name: str):
    # 取得伺服器物件
    guild = ctx.guild
    # 尋找指定頻道
    channel = discord.utils.get(guild.channels, name=channel_name)
    if channel:
        # 取得頻道中的所有訊息
        messages = await channel.history(limit=None).flatten()
        # 刪除所有訊息
        await channel.delete_messages(messages)
        await ctx.send(f'已清空 {channel_name} 頻道的所有訊息。')
    else:
        await ctx.send(f'找不到名稱為 {channel_name} 的頻道。')

# 當機器人成功登入時觸發的事件
@bot.event
async def on_ready():
    print(f'已成功登入：{bot.user.name} ({bot.user.id})')

# 定義一個函式來啟動機器人
def run_bot():
    # 載入機器人的 Token 並啟動機器人
    bot.run('YOUR_BOT_TOKEN')
