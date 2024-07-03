import discord
from discord.ext import commands

token = "gapi_pdKI6aY/M5z+Cmo1hXbZGKYy9Hy0QWb4mfAkdWZi5JUcblyQKaGPffYtX+UdQQE3fkLLYNaPXIFTrPfXaa9wEg==" # Token شما
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def play(ctx, song_name):
    voice_channel = ctx.author.voice.channel
    if voice_channel:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(song_name))
    else:
        await ctx.send("برای استفاده از این دستور باید در یک چنل صوتی باشید.")

client.run(token)