import discord
from discord.ext import commands
import io
import asyncio
import os
import time
from PbBot import botStartTime, Delete_after_duration

class BASH(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.has_role('Admin')       # Check for admin role before shell commands (Enable before merging to master)
    @commands.command() #for commands
    async def bash(self, ctx, *, cmd: str):
        author = ctx.message.author
        msg = await ctx.send('Running the task.')
        process = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        print(f'{cmd} command was run by {author} from chat {ctx.message.channel.name} of guild {ctx.message.guild}.')
        e = stderr.decode()
        if not e:
            e = "No Error"
        o = stdout.decode()
        if not o:
            o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
        else:
            _o = o.split("\n")
            o = "`\n".join(_o)
        OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
        if len(OUTPUT) > 2000:
            with io.BytesIO(str.encode(OUTPUT)) as out_file:
                out_file.name = "exec.text"
                await ctx.message.channel.send(file=discord.file('exec.text'))
        await ctx.message.delete()
        await msg.edit(content=f'{author.mention} I have sent your output to your DM.\n Command used : ```{cmd}```', Delete_after_duration)
        await author.send(f'{author.name} your output is here.\n{OUTPUT}')


def setup(client):
    client.add_cog(BASH(client))
