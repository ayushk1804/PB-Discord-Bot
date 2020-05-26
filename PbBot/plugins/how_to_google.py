# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import requests
import json
import os
import asyncio
from PbBot import Delete_after_duration

class HowToGoogle(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='How to Google', description='Teach them how to use google.', aliases=['htg'], brief='How to Google stuff', usage='.htg <Search query>' ) #for commands
    async def howToGoogle(self, ctx, *, input_str):
        if ctx.message.author == self.client:
            return
        msg = await ctx.send("I will guide you...")
        sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(input_str.replace(" ", "+"))
        response_api = requests.get(sample_url).text
        if response_api:
            await msg.edit(content="[{}]({})\n`Thank me Later 🙃` ".format(input_str, response_api.rstrip()))   # Use embeds to beautify this.
        else:
            await msg.edit(content="something is wrong. please try again later.")
        await ctx.message.delete()
        await asyncio.sleep(Delete_after_duration)
        await msg.delete()


def setup(client):
    client.add_cog(HowToGoogle(client))
