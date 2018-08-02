from config import *

class Bdsm():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def bdsm(self):
		sublist = ['BDSMGW',
				'bdsmgifs',
				'rough_sex_gifs',
				'bdsm_gif',
				'extreme_gifs',
				'bdsmgifs',
				'bdsm_gifs'
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
				print('Command `bdsm` executed. Subreddit used: `' + sub + '`. Post: ' + str(post))
			except:
				print('Error fetching image from ' + sub + '. Trying again. (post number: ' + str(post) + ') attempt: ' + str(attempts))
				attempts = attempts + 1

def setup(bot):
    bot.add_cog(Bdsm(bot))