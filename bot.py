#############
###Imports###
#############
import os
import random
import time
from datetime import datetime
from datetime import date

import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import Bot

################
###Bot Prefix###
################

client = commands.Bot(command_prefix = ".")

############################
###Bot Connection Message###
############################

@client.event
async def on_ready():
    print("Bot has connected to Discord!")
       
class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Game(name='Making bets!'))
        
##################################        
###When messages are being sent###  
##################################  

    async def on_message(self, message):
        
        messageContent = message.content
        
        ###########################################
        ###Stop bot replying to its own messages###
        ###########################################
        
        if message.author == self.user:
            return
       
            await message.channel.send(embed=embedVar)  
        
        #######################
        ###Setup the betting###
        #######################
        
        
        
        guild = ctx.message.guild
        await guild.create_text_channel('💵BetBot💵')
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)

        
        
        
        
        
        
        
        #################################
        ###Send A Message From The Bot###
        #################################
        
        if ".botsend" in messageContent:
            await message.delete()
            messageContent = messageContent.replace('.botsend', '')
            await message.channel.send(messageContent)
        
        ##########################
        ###Prints Help Commands###
        ##########################
        
        if ".help" in messageContent:
            embedVar = discord.Embed(title="Lads Discord Bot Help", description="Below are all the commands for the discord bot.", color=0x6a0dad)
            embedVar.add_field(name=".marry", value="This command is only accesable to @dyslexic#2467 and @sock_wok#4624. Use this command by typing ```.marry personA,Personb``` The comma is important to be used.", inline=False)
            embedVar.add_field(name=".divorce", value="This command is only accesable to @dyslexic#2467 and @sock_wok#4624. Use this command by typing ```.divorce [marriageNO]```", inline=False)
            embedVar.add_field(name=".mrecords", value="Displays the marriages and their marriage numbers", inline=False)
            embedVar.add_field(name=".hive", value="Genertaes a random Minecraft Bedrock Hive Game to play", inline=False)
            embedVar.add_field(name="More Bot commands soon", value=" Please suggest ideas by DMing or Pinging @AJC#2921", inline=False)
            await message.channel.send(embed=embedVar)
            
####################
###Discord Tokens### 
####################

client = MyClient()
client.run('Nzg1ODcyNjU3MTI0MDMyNTIy.X8-K8g.JwlOLGDG4WJMUQAYDGG7nhrq2dA')

#########
###END###
#########
