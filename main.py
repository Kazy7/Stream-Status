import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='+',
  self_bot=True
)



@client.event
async def on_connect():
  await Lucifer_404notfoundclient.change_presence(activity = discord.Streaming(name = "Sleeping", url = "https://www.twitch.tv/Kazy_777"))


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)


#made by Kazy777
