import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Habilita leitura de mensagens

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.command()
async def comands(ctx):
    mensagem = (
    "```"
    "─────────────── COMANDOS DISPONÍVEIS ───────────────\n"
    "\n"
    "1. Comando 1\n"
    "2. Comando 2\n"
    "3. Comando 3\n"
    "4. Comando 4\n"
    "5. Comando 5\n"
    "6. Comando 6\n"
    "\n"
    "─────────────── AÇÕES ───────────────\n"
    "Sair\n"
    "Chamar assistência\n"
    "```"
)
    await ctx.send(mensagem)

@bot.command()
async def sobre(ctx):
   mensagem = (
    "```"
    "─────────────── SOBRE ───────────────\n"
    "\n"
    "Este bot foi criado com o objetivo de auxiliar a oficial Myllena Areda em tarefas múltiplas\n"
    "que demandam agilidade e eficiência.\n"
    "\n"
    "Este bot não tem finalidade lucrativa ou comercial, sendo destinado ao uso local e disponível\n"
    "apenas para usuários autorizados pela oficial Myllena Areda Fernandes.\n"
    "\n"
    "Atividades suspeitas por usuários não autorizados serão devidamente investigadas e poderão\n"
    "resultar em providências cabíveis.\n"
    "\n"
    "Esta aplicação possui todos os direitos reservados e é proibida sua reprodução total ou parcial\n"
    "sem a autorização expressa da oficial Myllena Areda Fernandes.\n"
    "\n"
    "Aplicação desenvolvida por Livio Evangelista Da Costa Filho, que detém total acesso e liberdade\n"
    "para realizar quaisquer modificações, exclusões ou melhorias.\n"
    "```"
   )
   await ctx.send(mensagem)

bot.run(BOT_TOKEN)
