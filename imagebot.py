import praw
import random
from discord.ext import commands
import asyncio

# Begin bot configuration
# 
bot = commands.Bot(description="BOT DESCRIPTION GOES HERE", command_prefix="!") # Change description and command prefix to suit
token = 'DISCORD BOT USER TOKEN GOES HERE' 	# Remove before uploading
reddit = praw.Reddit(client_id='REDDIT BOT CLIENT ID GOES HERE', 						# Remove before uploading
					client_secret='REDDIT BOT CLIENT SECRET GOES HERE',		# Remove before uploading
					user_agent='REDDIT BOT NAME GOES HERE - MUST BE UNIQUE')							# Remove before uploading
# End bot configuration. Do not edit below unless you know what you are doing
# ############################################################################
# ############################################################################

@bot.event
async def on_ready():
	print('Logged in as')
	print('Username: ' + bot.user.name)
	print('Client ID: ' + bot.user.id)
	print('--------------')
	print('TKP Image Bot READY!')
					 
@bot.command()
async def cum():
	sublist = ['PrettyCumSluts',
			'AmateurCumsluts',
			'GWCumsluts',
			'cumsluts',
			'GirlsFinishingTheJob',
			'unexpectedcum',
			'party_facials',
			'before_after_cumsluts',
			'cumfetish',
			'cumonclothes',
			'Cumtyphoon'
			]
	sub = random.choice(sublist)
	image = reddit.subreddit(sub).new()
	post_to_pick = random.randint(1, 50)
	for i in range(0, post_to_pick):
		submission = next(x for x in image if not x.stickied)
		
	await bot.say(submission.url)
	print('Command `cum` executed. Subreddit used: `' + sub + '`.')

bot.run(token)
