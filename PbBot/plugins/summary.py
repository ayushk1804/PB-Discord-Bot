# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780
# co-author : Nikhil Kumar - @NIK-99

import discord
from discord.ext import commands
from summa import summarizer
import urllib3
from bs4 import BeautifulSoup
import io
from PbBot import Delete_after_duration

class Summary(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='Summary', aliases=['tldr'], brief='.tldr <del.dog link> <% of text for summary>', description='tl;dr - Sometimes texts are just too long to read so we need a quick summary. Read Ratio means the length of text that the summary should be w.r.t original text. This module uses AI to generate a summary of your text. Make sure to paste your text in del.dog before using this command.')
    async def _summary(self, ctx, link, read_ratio: int = 20):
        try:
            if 'del.dog' not in link:
                await ctx.send('Paste your text in del.dog!', delete_after=Delete_after_duration)
            def fg(url):
                def response_getter(url):
                    http = urllib3.PoolManager()
                    response = http.request('GET', url)
                    return response
                res = response_getter(url)
                soup = BeautifulSoup(res.data, 'html.parser')
                z = soup.find(class_ ="chroma")             # print(soup.find(class_='paste_code').contents[0])- pastebin
                return z.contents[0]
            txt = fg(link)
            gen_summary = summarizer.summarize(txt, ratio=(read_ratio/100))
            if len(gen_summary)>1500:
                with io.BytesIO(str.encode(gen_summary)) as out_file:
                    out_file.name = f'Summary for {link}.txt'
                    await ctx.send(file=discord.File(out_file), delete_after=6*Delete_after_duration)
            else:
                await ctx.send(gen_summary, delete_after=6*Delete_after_duration)
            with io.BytesIO(str.encode(gen_summary)) as out_file:
                out_file.name = f'Summary for {link}.txt'
                await ctx.message.author.send(file=discord.File(out_file))
        except Exception as e:
            print(e)        # TODO implement logger here
        finally:
            await ctx.message.delete()


def setup(client):
    client.add_cog(Summary(client))
