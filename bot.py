import os
import discord

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
