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
import psutil

# from Bots.Discord.bot import botStartTime # implement later

class BotStats(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='BotStats', description='Give useful bot sys info! Delete duration is set to twice the global duration', aliases=['bstats'], brief='.bstats gives some basic bot stats')
    async def bstats(self, ctx):
        original_msg = ctx.message
        msg = await ctx.send("Checking Bot Stats!")
        cpufreq = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        currentTime = time.time()-botStartTime
        total, used, free = shutil.disk_usage('.')
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        stats = f'```Bot Uptime: {get_readable_time(currentTime-botStartTime)}```' \
                f'```Disk Information:\nTotal disk space: {total}' \
                f'\tUsed: {used}' \
                f'\tFree: {free}```'
        stats += f'```CPU Information:\nPhysical cores:{psutil.cpu_count(logical=False)}\tTotal cores: {psutil.cpu_count(logical=True)}\tMax Frequency: {cpufreq.max:.2f}Mhz\nMin Frequency: {cpufreq.min:.2f}Mhz\tCurrent Frequency: {cpufreq.current:.2f}Mhz```'
        stats += f'```Memory Information\nTotal: {humanbytes(svmem.total)}\tAvailable: {humanbytes(svmem.available)}\tUsed: {humanbytes(svmem.used)}\tPercentage: {svmem.percent}%\n```'
        stats += f'```Swap Information\nTotal: {humanbytes(swap.total)}\tAvailable: {humanbytes(swap.free)}\tUsed: {humanbytes(swap.used)}\tPercentage: {swap.percent}%```'
        await asyncio.sleep(1.5)
        await msg.edit(content=stats, delete_after=(Delete_after_duration)*3)
        await original_msg.delete()


def setup(client):
    client.add_cog(BotStats(client))
