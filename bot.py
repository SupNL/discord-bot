import discord
import json
from discord.ext import commands

client = commands.Bot(command_prefix = '')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        return
    raise error

@client.event
async def on_ready():
    print('Bot is ready!!')

@client.command(aliases=['lilil', 'lililil', 'lilililil'])
async def responder(ctx):
    await ctx.send(ctx.message.content)

try:
    with open('botData.json', 'r') as file:
        data = json.loads(file.read())
        client.run(data['token'])
except FileNotFoundError:
    print('Error: botData.json not found')
except discord.errors.LoginFailure:
    print('Error: Invalid token')


