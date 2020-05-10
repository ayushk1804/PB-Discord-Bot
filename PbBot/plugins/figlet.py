#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
try:
    import pyfiglet
    import asynio
except:
    import os
    os.system('pip install pyfiglet')
    os.system('pip install asyncio')
    try:
        import pyfiglet
        import asyncio
    except:
        pass

from PbBot import Delete_after_duration

# TODO: Implement logger.

class Figlet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='figlet',
                      description='Figlets are awesome. Try them . Available commands are like .figlet {text}|{font type} , where font type are ["slant", "3D", "5line", "alpha", "banner","doh", "iso", "letter", "allig", "dotm", "bubble" "bulb", "digi"]. Choose away! :fire:',
                      aliases=['fig'],
                      brief='.fig <text>|<style>',
                      usage='.fig [text]|[style]')
    async def figlet_str(self, ctx, *, input_str):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.message.delete()
        msg = await ctx.send("FIGLET!!")
        CMD_FIG = {"slant": "slant", "3D": "3-d", "5line": "5lineoblique", "alpha": "alphabet", "banner": "banner3-D",
                   "doh": "doh", "iso": "isometric1", "letter": "letters", "allig": "alligator", "dotm": "dotmatrix",
                   "bubble": "bubble", "bulb": "bulbhead", "digi": "digital", "big": "big"}
        if "|" in input_str:
            text, cmd = input_str.split("|", maxsplit=1)
        elif input_str is not None:
            cmd = None
            text = input_str
        else:
            await msg.edit(content="Please add some text to figlet", delete_after=(Delete_after_duration/2))
            return
        if cmd is not None:
            try:
                font = CMD_FIG[cmd]
            except KeyError:
                await msg.edit(content="Invalid selected font.", delete_after=(Delete_after_duration/2))
                return
            result = pyfiglet.figlet_format(text, font=font)
        else:
            result = pyfiglet.figlet_format(text)
        if len(result) >= 2000:
            return await ctx.send(
                f'Error: ASCII\'s count is {len(result)}. Discord\'s limitation is 2000 only.', delete_after=Delete_after_duration)
        elif len(text) >= 14:
            await msg.edit(content="Warning: It's better not to exceed 14 characters, otherwise this will look terrible for mobiles devices. If you still agree to go forward, please say `yes` (within 30 secs).")
            try:
                confirm_text = await ctx.bot.wait_for("message", check=check, timeout=30)
                if confirm_text.content.lower() != "yes":
                    return await ctx.send("Okay. Won't do this", delete_after=Delete_after_duration)
            except asyncio.TimeoutError:
                await msg.delete()
                return await ctx.send("You took too long to reply!", delete_after=Delete_after_duration)
        await msg.edit(content=f'‌‌‎`{result}`')


def setup(client):
    client.add_cog(Figlet(client))
