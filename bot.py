import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

token = "NTI0OTY3MDE3NzgzMDk5NDEy.Dvv17g.BxXD5GhVA1eTSxIhuKLD1cFmrgU"
userID  = 243038734583463936

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    
    if message.content.lower().startswith('-r'):
        args = message.content.split(" ")
        #args[0] = -r
        #args[1] = 1d6
        dice_mod = args[len(args)-1]
        try:
            dice = dice_mod.split('+')[0]
        except ValueError:
            dice = dice_mod
        #dice[0] = 1
        #dice[2] = 6
        i = 0
        qtd,size_mod = dice_mod.split('d')
        qtd = int(qtd)
        try:
            size,mod = size_mod.split('+')

        except ValueError:
            size = size_mod
            mod = 0
        
        size = int(size)
        mod = int(mod)
        rolls = []
        s = 0
        for i in range(qtd):
            roll = random.randint(1,size)
            rolls.append(roll)
            s += roll
        s+=mod
        rolls = str(rolls)
        if mod != 0:
            await client.send_message(message.channel," ``` %s + %i = %i. %s```"  %(dice,mod,s,rolls))
        else:
            await client.send_message(message.channel," ``` %s = %i. %s```"  %(dice,s,rolls))

client.run(token) #Replace token with your bots token