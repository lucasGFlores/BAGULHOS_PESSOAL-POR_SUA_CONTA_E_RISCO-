import math as mt
import Ferramentas as fr
import Banco as bd
import discord
from discord.ext import commands
def girarPoder(idUser,idP,idM, texto= ''):
        dado = bd.dadoMassa(idUser,idP,idM)
        atri = bd.converterAtriParaMod(idUser,idP,idM)
        if texto == '':
            texto = bd.nomeDaMagia(idUser,idP,idM)    
        if (atri) > 0:
            fr.dado(f"{dado}+{int(atri)}",texto)
        else:
            fr.dado(f"{dado}{atri}",texto) 
bot = commands.Bot("J")    
@bot.event
async def on_ready():
    print(f"estou aqui caralho, no corpo de {bot.user}")
@bot.command(name = "eae" )
async def eae(ctx):
    await ctx.send(f"Eae {ctx.author.name}")
bot.run('OTQ3OTQ3OTc1ODUyODQ3MTQ0.Yh0rWQ.keWIFVoCFq5TwEBmEMEXsKiQSlU')





    
    


