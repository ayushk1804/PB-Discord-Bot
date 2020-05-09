#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#(c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import glob
from PbBot import Delete_after_duration

class Alive(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name='Alive', decription='Check if bot is Alive', brief='.alive to check bot status', usage='.alive')
    async def alive(self,ctx):
        await ctx.message.delete()
        await ctx.send(f':robot: Bot is Working and has {len(glob.glob("./PbBot/plugins/*.py"))} plugin(s) installed.', delete_after=(Delete_after_duration/2))
    #@commands.command() #for commands
    #@commands.Cog.listener #for event listener


def setup(client):
    client.add_cog(Alive(client))
