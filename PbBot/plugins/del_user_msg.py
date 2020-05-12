  
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
from PbBot import Delete_after_duration

class DeleteSpecificUser(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='deleteSpecificUserMessage', description='Try to delete a specific user message', brief='Delete user messages .delmsgfrom @<user> <no of msgs to be deleted.>', aliases=['delsumsg', 'delmsgfrom'], usage='.delmsgfrom [@user] <no of messages to delete>')
    async def delusermsg(self, ctx, member: discord.Member, no_of_messages):
        if ctx.message.author == self.client:
            return
        channel = ctx.message.channel
        count = 0
        try:
            for _ in range(int(no_of_messages)):
                count += 1
                del_msg = await channel.history().get(author=member)
                await del_msg.delete()
        except Exception as e:
            await ctx.send(f'{ctx.message.author.mention}, deleted {count} messages and then some error occurred...', delete_after=Delete_after_duration)
        else:
            await ctx.send(f'{ctx.message.author.mention}, deleted {count} messages successfully...', delete_after=Delete_after_duration)
        await ctx.message.delete()


def setup(client):
    client.add_cog(DeleteSpecificUser(client))
