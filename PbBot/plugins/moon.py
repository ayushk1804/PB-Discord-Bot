#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import asyncio
from collections import deque
from PbBot import Delete_after_duration


class PlanetAnimations(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='smoon', aliases=['animoon'])
    async def smooon(self, ctx):
        await ctx.message.delete()
        animation_interval = 1
        animation_ttl = range(0, 32)

        msg = await ctx.send("Animating moon Phases!")

        animation_chars = [

            "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
            "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
            "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
            "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
            "🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
            "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
            "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
            "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖"
        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await msg.edit(content=str(animation_chars[i % 8]))
        await asyncio.sleep(Delete_after_duration)
        await msg.delete()

    @commands.command(name='tmoon', aliases=['animoon2'])
    async def tmoon(self, ctx):
        await ctx.message.delete()
        animation_interval = 1
        animation_ttl = range(0, 33)
        msg = await ctx.send("Animating Moon Faces!")

        animation_chars = [

            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖"
        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)

            await msg.edit(content=animation_chars[i % 33])
        await asyncio.sleep(Delete_after_duration)
        await msg.delete()

    @commands.command(name='earth', aliases=['animearth'])
    async def aniearth(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send('Earth animated!')
        deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
        for _ in range(48):
            await asyncio.sleep(1)
            await msg.edit(content=f'{"".join(deq)}', delete_after=Delete_after_duration)
            deq.rotate(1)

    @commands.command(name='PointBlank!', aliases=['pb'], brief='.pb <delete after interval> default=10secs')
    async def point_blank(self, ctx, del_interval: int = Delete_after_duration):
        author = ctx.message.author
        await ctx.message.delete()
        animation_interval = 1
        animation_ttl = range(0, 8)

        msg = await ctx.send(f"{author.mention}, Welcome to PB!!")

        animation_chars = [
            "GSOC",
            "ACM-ICPC",
            "Codeforces",
            "CodeChef",
            "CodeJam",
            "KickStart?",
            "GSOD",
            "PB - A DSCE CODE COMMUNITY"
        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await msg.edit(content=str(animation_chars[i % 8]))
        await asyncio.sleep(del_interval)
        await msg.delete()


def setup(client):
    client.add_cog(PlanetAnimations(client))
