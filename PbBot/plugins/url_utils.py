#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

"""DA.GD helpers
Available Commands:
.surl <long url>
.unshort <short url>"""

import discord
from discord.ext import commands
import requests
import re
from PbBot import Delete_after_duration


URL_REGEX = r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+"
# URL_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'  # identify urls
# MAGNET_REGEX = r"magnet:\?xt=urn:btih:[a-zA-Z0-9]*"   # for implementing magnet handling :p if we ever do it.

class Url_Utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='Shortner', description='Url Shortner working on da.gd',
                      aliases=['surl', 'shorturl', 'shortlink'], brief='.surl <long url> will generate a short url')
    async def shorturl(self, ctx, *, url):
        def shurl(link):
            sample_url = f'https://da.gd/s?url={link}'
            response_api = requests.get(sample_url).text
            if response_api:
                return "Generated {} for {}.".format(response_api, link)
            else:
                return "something is wrong. please try again later."

        if ' ' in url:
            msg = await ctx.send("Sent multiple URLS. :sob:")
            urls = re.findall(URL_REGEX, url)
            shorts = []  # successful short urls
            ushorts = []  # unsuccessful short urls
            for i in urls:
                z = shurl(i)
                if 'something is wrong' in z:
                    ushorts.append(z)
                else:
                    shorts.append(z)
            short_url_list = ''
            unsuccessful_list = ''
            for u in range(len(shorts)):
                short_url_list += '{u+1}. {shorts[u]}\n'
            for uns in range(len(ushorts)):
                unsuccessful_list += '{u+1}. {shorts[u]}\n'
            await msg.edit(
                content=f'Successfully shortened {len(shorts)} urls.\nSuccessful :\n{short_url_list}\n\nUnsuccessful :\n{unsuccessful_list}')
        else:
            if re.match(URL_REGEX, url):
                msg = await ctx.send("Shortening!!")
                await msg.edit(content=shurl(url))
            else:
                await ctx.send("CHECK URL!! :confused:", delete_after=Delete_after_duration)
        return

    @commands.command(name='Un-Shortner', description='Url Un-Shortner working on da.gd',
                      aliases=['lurl', 'longurl', 'furl'], brief='.lurl <long url> will generate a short url')
    async def unshort(self, ctx, *, url):
        msg = await ctx.send("Trying to get Full URL...")
        if not url.startswith("http"):
            url = "http://" + url
        r = requests.get(url, allow_redirects=False)
        if str(r.status_code).startswith('3'):
            await msg.edit(content="Input URL: {}\nReDirected URL: {}".format(url, r.headers["Location"]))
        else:
            await msg.edit(content="Input URL {} returned status_code {}".format(url, r.status_code), delete_after=Delete_after_duration)

    @commands.command(name='UploadToOshi', description='Upload bot internal files to oshi.at', aliases=['oshi', 'fileupload'], brief='.oshi <file path> will get file url')
    async def fupload(self, ctx, *, filepath):
        author = ctx.message.author
        print(filepath)
        async def single_upload(path, ctx):
            msg = await ctx.send("Trying...")
            cmd = OSHI_GEN_URL.format(path)
            status_message = await ctx.send('Running the task.')
            process = await asyncio.create_subprocess_shell(
                cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            e = stderr.decode()
            o = stdout.decode()
            print(e, o)
            # if e:
            #     print(e)
            #     await ctx.send(f'Error generated. \n{e}', delete_after=10.0)
            #     return
            if o:
                # _o = o.split("\n")
                # o = "`\n".join(_o)
                await msg.edit(content=f'{author.mention} I have sent your output to your DM.', delete_after=Delete_after_duration)
                await author.send(f'{author.mention} your output is here.\n Uploaded: {filepath}\n```{o}```')
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            await single_upload(filepath, ctx)      # Can be used for performing Multiple Uploads.
            # msg = await ctx.send("Please enter the file name (Path is preferred). Max File size is 1GB.")
            # confirm_text = await ctx.bot.wait_for("message", check=check)
            # if confirm_text.content.lower():
            #     try:
            #         filesList = glob2.glob(f'./**/{confirm_text.content}', recursive=True)
            #         if len(filesList) == 0:
            #             await ctx.send(f'File not found. Retry...', delete_after=10.0)
            #         elif len(filesList)>1:
            #             await ctx.send(f"Mutiple Files found. Please enter File Path", delete_after=10.0)
            #             info = discord.Embed(title=f'Announcement!', color=0x992D22)
            #             info.add_field(name="Files List", value=filesList)
            #             await ctx.send(embed=info, delete_after=60.0)
            #         else:
            #
            # await confirm_text.delete()

        except Exception as e:
            print(e)
            
            
def setup(client):
    client.add_cog(Url_Utilities(client))
