#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import random
from PbBot import Delete_after_duration

class Belo(commands.Cog):

    def __init__(self, client):
        self.client = client

    # for command listening
    @commands.command(name='Belo', description='Gives out a random(not really) sentance, Delete duration is set to twice the global duration', aliases=[], brief='.belo - takes no arguments gives out a random sentence')
    async def belo(self, ctx):
        author = ctx.message.author
        await ctx.message.delete()
        sayings = ["Underwater bubbles and raindrops are total opposites of each other.",
                   "If you buy an eraser you are literally paying for your mistakes.",
                   "The Person you care for most has the potential to destroy you the most.",
                   "If humans colonize the moon, it will probably attract retirement homes as the weaker gravity will allow the elderly to feel stronger.",
                   "Any video with “wait for it” in the title is simply too long."]
        await ctx.send(f'{author.mention} Here is something to munch on:\n```{random.choice(sayings)}```', delete_after=Delete_after_duration*2)

    # @commands.Cog.listener # for event listener


def setup(client):
    client.add_cog(Belo(client))
