#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import time
import shutil
from PbBot.utils.utils import humanbytes, get_readable_time
import asyncio
from PbBot import botStartTime, Delete_after_duration

# from Bots.Discord.bot import botStartTime # implement later

class BotStats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='BotStats', description='Give useful bot sys info! Delete duration is set to twice the global duration', aliases=['bstats'], brief='.bstats gives some basic bot stats')
    async def bstats(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send("Checking Bot Stats!")
        currentTime = time.time()-botStartTime
        total, used, free = shutil.disk_usage('.')
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        stats = f'Bot Uptime: {get_readable_time(currentTime)}\n' \
                f'Total disk space: {total}\n' \
                f'Used: {used}\n' \
                f'Free: {free}'
        await asyncio.sleep(1.5)
        await msg.edit(content=stats, delete_after=(Delete_after_duration)*2)


def setup(client):
    client.add_cog(BotStats(client))
