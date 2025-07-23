from discord.ext import commands
from core import messages

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def comands(self, ctx):
        await ctx.send(messages.COMANDOS)

    @commands.command()
    async def sobre(self, ctx):
        await ctx.send(messages.SOBRE)

async def setup(bot):
    await bot.add_cog(Comandos(bot))
