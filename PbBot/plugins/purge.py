#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands


class Purge(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.has_role('SudoUsers')
    # @commands.has_permissions(discord.permissions.Permissions.manage_channels)
    @commands.command(name='purge', description='A basic purge command', brief='.purge <number> deletes last 5 messages by default')  # for commands
    async def purge(self, ctx, amount=5):
        try:
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)
        except:
            await ctx.send(f'Could not purge', delete_after=10.0)

def setup(client):
    client.add_cog(Purge(client))
