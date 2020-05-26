# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import os

class Fetch_logs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='getLogs')       # for commands
    async def get_logs(self, ctx):
        try:
            if ctx.message.author == self.client:
                return
            else:
                try:
                    await ctx.send(file=discord.File(f'./logs/discord.log'))         # change the path for actual log file
                    # await ctx.message.author.send(file=discord.File(f'./utils.py'), delete_after=10.0)         # change the path for actual log file
                except Exception as e:
                    print(e)
        except Exception as e1:
            print(f'E1: {e1}')
        await ctx.message.delete()
    # @commands.Cog.listener #for event listener

def setup(client):
    client.add_cog(Fetch_logs(client))
