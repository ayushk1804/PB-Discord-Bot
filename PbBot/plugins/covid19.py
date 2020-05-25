# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
import datetime
import requests

from PbBot import Delete_after_duration

class Corona(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='Corona', aliases=['c0','covid19'])
    async def _corona(self, ctx):
        message = await ctx.send('Corona :sob:')
        try:
            r = requests.get("https://corona.lmao.ninja/v2/all?yesterday=true").json()
            last_updated = datetime.datetime.fromtimestamp(r['updated'] / 1000).strftime("%Y-%m-%d %I:%M:%S")

            global_stats = discord.Embed(title='Global Statistics', color=0x992D22)
            global_stats.set_author(name='Corona API', url='https://corona.lmao.ninja', icon_url='https://da.gd/n331bG')
            global_stats.set_thumbnail(url='https://da.gd/JkNo')
            global_stats.set_footer(text=f'Last updated on: {last_updated}', icon_url='https://da.gd/hYhbH')
            global_stats.add_field(name='Cases', value=f"{r['cases']}")
            global_stats.add_field(name='Cases Today', value=f"{r['todayCases']}")
            global_stats.add_field(name='Deaths Today', value=f"{r['todayDeaths']}")
            global_stats.add_field(name='Recovered', value=f"{r['recovered']}")
            global_stats.add_field(name='Active', value=f"{r['active']}")
            global_stats.add_field(name='Critical', value=f"{r['critical']}")
            global_stats.add_field(name='Cases/Million', value=f"{r['casesPerOneMillion']}")
            global_stats.add_field(name='Deaths/Million', value=f"{r['deathsPerOneMillion']}")
            global_stats.add_field(name='Tests', value=f"{r['tests']}")
            global_stats.add_field(name='Tests/Million', value=f"{r['testsPerOneMillion']}")

            await message.edit(content=None, embed=global_stats, delete_after=Delete_after_duration)
        except Exception as e:
            await message.edit(content="```The corona API could not be reached```", delete_after=Delete_after_duration)
            print(e)
        await ctx.message.delete()

    @commands.command(name='Corona_search', aliases=['cs0', 'covidsearch'])
    async def _corona_search(self, ctx, country: str):
        if ctx.message.author == self.client:
            return

        if len(country) < 2:
            await ctx.send('```Not enough params provided```', delete_after=Delete_after_duration)
            await ctx.message.delete()
            return

        message = await ctx.send(f"```Getting Corona statistics for {country}```")
        try:
            r = requests.get(f"https://corona.lmao.ninja/v2/countries/{country.lower()}").json()
            if "cases" not in r:
                await message.edit(content="```The country could not be found!```", delete_after=Delete_after_duration)
            else:
                last_updated = datetime.datetime.fromtimestamp(r['updated'] / 1000).strftime("%Y-%m-%d %I:%M:%S")
                country = r['countryInfo']['iso3'] if len(r['country']) > 12 else r['country']
                stats = discord.Embed(title=f'Corona Stats for {country.capitalize()} ', color=0x992D22)
                stats.set_author(name='Corona API', url='https://corona.lmao.ninja', icon_url='https://da.gd/n331bG')
                stats.set_thumbnail(url='https://da.gd/JkNo')
                stats.set_footer(text=f'Last updated on: {last_updated}', icon_url='https://da.gd/hYhbH')
                stats.add_field(name='Cases', value=f"{r['cases']}")
                stats.add_field(name='Cases Today', value=f"{r['todayCases']}")
                stats.add_field(name='Deaths Today', value=f"{r['todayDeaths']}")
                stats.add_field(name='Recovered', value=f"{r['recovered']}")
                stats.add_field(name='Active', value=f"{r['active']}")
                stats.add_field(name='Critical', value=f"{r['critical']}")
                stats.add_field(name='Cases/Million', value=f"{r['casesPerOneMillion']}")
                stats.add_field(name='Deaths/Million', value=f"{r['deathsPerOneMillion']}")
                stats.add_field(name='Tests', value=f"{r['tests']}")
                stats.add_field(name='Tests/Million', value=f"{r['testsPerOneMillion']}")
                await message.edit(content=None, embed=stats, delete_after=Delete_after_duration)
        except Exception as e:
            await message.edit(content="```The corona API could not be reached```", delete_after=Delete_after_duration)
            print(e)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Corona(client))
