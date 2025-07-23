from discord.ext import commands
from core.groq_api import perguntar_groq


class Duvidas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def duvidas(self, ctx, *, pergunta: str):
        resposta = perguntar_groq(pergunta)
        await ctx.send(resposta)
async def setup(bot):
    await bot.add_cog(Duvidas(bot))