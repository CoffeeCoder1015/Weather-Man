import f_opt

from discord.ext import commands
import discord

client = commands.Bot(command_prefix="WMAN")

def run(ID,mode):
    client.run(ID,bot=mode)

#option set to file name - 
#so below only works when the script is ran with the exact file name - no "\", ".\", etc
f_opt.f_opt({
    "WeatherMan.py":([str,bool],run)
})