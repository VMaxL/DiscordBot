import discord
import validators
import os
from dotenv import load_dotenv
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Embed a link on the given text in format: `[text][space][link]
    if message.content.startswith('`'):
        dt = message.content[1:].split()
        if len(dt) >= 2 and validators.url(dt[len(dt)-1]):
            embedVar = discord.Embed(title=' '.join(dt[0:-1]), color=0x3498db, url=dt[len(dt)-1])
            await message.channel.send(embed=embedVar)
            await message.delete()
        if not validators.url(dt[len(dt)-1]):
            await message.channel.send("No link detected")

    custom_emojis = re.findall(r'<:\w*:\d*>', message.content)
    if custom_emojis is not []:
        for emoji in custom_emojis:
            await message.add_reaction(emoji)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)

