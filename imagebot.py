from config import *

@bot.event
async def on_ready():
	cogs = ''
	print('Logged in as')
	print('Username: ' + bot.user.name)
	print('Client ID: ' + bot.user.id)
	print('--------------')
	loadedmods = ''
	for extension in modules:
		print('Extension loaded: ' + extension[5:])
	print('TKP Image Bot READY!')

@bot.command()
async def load(extension_name : str):
	try:
		bot.load_extension(extension_name)
	except (AttributeError, ImportError) as e:
		await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await bot.say("```{} loaded.```".format(extension_name))

@bot.command()
async def unload(extension_name : str):
	bot.unload_extension(extension_name)
	await bot.say("```{} unloaded.```".format(extension_name))
	
@bot.command()
async def reload(extension_name : str):
	bot.unload_extension(extension_name)
	try:
		bot.load_extension(extension_name)
	except (AttributeError, ImportError) as e:
		await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
		return
	await bot.say("```{} reloaded.```".format(extension_name))

if __name__ == "__main__":
	for extension in modules:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(token)