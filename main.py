
import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

await bot.add_cog(Greetings(bot))


client.run(os.getenv('DISCORD_API_KEY'))
