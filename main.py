
import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    await message.channel.send(f'Hello, {member}!')

client.run(os.getenv('DISCORD_API_KEY'))