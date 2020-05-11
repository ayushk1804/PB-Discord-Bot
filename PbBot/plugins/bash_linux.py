import discord
from discord.ext import commands
import io
import asyncio
import os
import time
from PbBot import Delete_after_duration


class BASH(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.has_role('Admin')
    @commands.command(name='bash', description='A linux bash subprocess (dont try to use sudo)', brief='bash | .bash <command> ', usage='.bash [command]')
    async def bash(self, ctx, *, cmd: str):
        author = ctx.message.author
        msg = await ctx.send('Running the task.')
        if 'sudo' in cmd:
            return await msg.edit(f"{author.mention}, dont Try to run Sudo commands", delete_after=Delete_after_duration)
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
        OUTPUT = f"**QUERY:**\n__Command:__```{cmd}``` \n__PID:__```{process.pid}```\n**stderr:** ```{e}```\n**Output:**```{o}```"
        if len(OUTPUT) > 2000:
            with io.BytesIO(str.encode(OUTPUT)) as out_file:
                out_file.name = "exec.text"
                await ctx.message.channel.send(file=discord.file('exec.text'))
        await ctx.message.delete()
        await msg.edit(content=f'{author.mention} I have sent your output to your DM.\n Command used : ```{cmd}```', delete_after=Delete_after_duration)
        await author.send(f'{author.name} your output is here.\n{OUTPUT}')


def setup(client):
    client.add_cog(BASH(client))
