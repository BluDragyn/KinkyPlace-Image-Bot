import discord
from discord.ext import commands
import praw
import asyncio
import random
import string

modules = ["cogs.cum",
		"cogs.boobs"
		]
bot = commands.Bot(description="Custom Image bot www.TheKinkyPlace.net", command_prefix="!")
token = 'PUT YOUR DISCORD TOKEN HERE'

reddit = praw.Reddit(client_id='REDDIT CLIENT ID',
					client_secret='REDDIT CLIENT SECRET',
					user_agent='REDDIT CLIENT NAME')
