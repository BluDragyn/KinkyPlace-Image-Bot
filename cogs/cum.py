from config import *

class Cum():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cum(self):
		sublist = ['PrettyCumSluts',
				'AmateurCumsluts',
				'GWCumsluts',
				'cumsluts',
				'GirlsFinishingTheJob',
				'unexpectedcum',
				'before_after_cumsluts',
				'cumfetish',
				'cumonclothes',
				'Cumtyphoon',
				'Cumontits',
				'FacialFun'
				]
		attempts = 1
		while attempts < 5:
			try:
				sub = random.choice(sublist)
				image = reddit.subreddit(sub).hot()
				post = random.randint(1, 75)
				for i in range(0, post):
					submission = next(x for x in image if not x.stickied)
	
				await self.bot.say(submission.url)
				attempts = 5
			except:
				attempts = attempts + 1

def setup(bot):
    bot.add_cog(Cum(bot))
