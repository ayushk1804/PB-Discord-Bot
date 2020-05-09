#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import time

# TODO: implement time zones

class BotTime(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='Time', description='Get Bot Time', brief='.btime | Get bot time.', usage='.btime')
    async def btime(self, ctx):
        await ctx.send(f'{time.asctime()}')
        await ctx.message.delete()
    # @commands.Cog.listener #for event listener


def setup(client):
    client.add_cog(BotTime(client))
