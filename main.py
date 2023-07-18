import discord
import os

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTEzMDcxMjE4NDcyMTI2NDczMg.GccfE2.bNT8GKdA8Z26O8vjfekNyDeTK3E2gw_CbAjbFk')
