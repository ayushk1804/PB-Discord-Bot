#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
from PbBot import Delete_after_duration


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ping', description='A simple ping', aliases=['p'], brief='.ping to get server latency.')
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! {round(self.client.latency * 1000,2)}ms', delete_after=Delete_after_duration)
        await ctx.message.delete()
        return

def setup(client):
    client.add_cog(Ping(client))
