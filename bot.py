import os
from threading import Thread
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'成功登入！目前身份：{client.user}')


@client.event
async def on_member_join(member):
  channel_id = 1530789227678269581  # 填入您的頻道 ID
  channel = member.guild.get_channel(channel_id)
  if channel:
    await channel.send(f'又有一個人來尋找他心愛的少女了呢... {member.mention} 記得來找我升sen值！')


# 從 Render 的環境變數安全讀取 Token
client.run(os.getenv('DISCORD_TOKEN'))

# 1. 建立一個簡單的 Flask 應用程式
app = Flask('')


@app.route('/')
def home():
  return "Bot is active and running!"


def run():
  # Render 會透過環境變數指定 Port，若沒有則預設用 8080
  port = int(os.environ.get('PORT', 8080))
  app.run(host='0.0.0.0', port=port)


def keep_alive():
  t = Thread(target=run)
  t.start()


# 2. 初始化你的 Discord 機器人
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
  print(f'目前登入身分：{bot.user}')


# 3. 主程式進入點
if __name__ == '__main__':
  # 啟動網頁伺服器（保活機制）
  keep_alive()

  # 啟動 Discord 機器人（請將 TOKEN 換成你的環境變數或字串）
  bot.run(os.environ.get('DISCORD_TOKEN'))
