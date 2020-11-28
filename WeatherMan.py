import f_opt

from discord.ext import commands
import discord
import asyncio
import find

client = commands.Bot(command_prefix="WMAN-")

@client.command()
async def current (ctx):
    msg = await ctx.send("Searching")
    data = find.currentWeather()
    await msg.edit(content=str(f"{data[0]}\n{data[1]}\n{data[2]}"))
   

def run(ID,mode):
    client.run(ID,bot=mode)

#option set to file name - 
#so below only works when the script is ran with the exact file name - no "\", ".\", etc
f_opt.f_opt({
    "WeatherMan.py":([str,bool],run)
})