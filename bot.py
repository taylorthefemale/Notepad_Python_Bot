#https://realpython.com/how-to-make-a-discord-bot-python/
#bot.py
import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

bot = commands.Bot(command_prefix='!')

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
	guild = ctx.guild
	existing_channel = discord.utils.get(guild.channels, name=channel_name)
	if not existing_channel:
		print(f'Creating a new channel: {channel_name}')
		await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send('You ain\'t no admin, don\'t front.')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
	brooklyn_99_quotes= [
		'I\'m the human form of the 💯 emoji.',
		'Bingpot!',
		'Sarge, with all due respect, I am gonna completely ignore everything you just said.',
		'A place where everybody knows your name is hell.',
		(
			'Cool. cool cool cool cool cool cool cool,'
			'no doubt no doubt no doubt no doubt.'
		),
	]

	response = random.choice(brooklyn_99_quotes)
	await ctx.send(response)

@bot.command(name='craps', help='A weak substitute for a gambler in withdraw...')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
	dice = [
		str(random.choice(range(1, number_of_sides +1)))
		for _ in range(number_of_dice)
	]
	await ctx.send(', '.join(dice))

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)

