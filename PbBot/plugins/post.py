#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands
from datetime import datetime
from PbBot import Delete_after_duration, AUTH_CHANNEL

#TODO: Implement database to store chanels and sudo users

channels = [int(AUTH_CHANNEL)]
Sudo_user = [259370246681395210, 645189639430340609]

class Announce(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='Announce', description='Announce to channels', aliases=['ann'], usage='.ann [message]')
    async def post(self, ctx, forrole: discord.Role, *, message: str):
        author = ctx.message.author
        await ctx.message.delete()
        def msgformat(msg: str):
            msg = msg.split()
            title = msg[0]
            body = ' '.join(msg[1:])
            return [title, body]

        print(str(message))
        if len(Sudo_user) > 0:
            if author.id in Sudo_user:  # compare usernames
                # if True:
                await ctx.send('User auth - :ok:', delete_after=(Delete_after_duration/2))
                [mtitle, body] = msgformat(message)
                # body += f'\n\n For:{forrole}\n \nBy:{ctx.message.author.mention}'
                try:
                    for chan in channels:
                        try:
                            channel = self.client.get_channel(chan)
                            
                            # info = discord.Embed(title=f'Announcement! - {mtitle}', description=body, color=0x992D22)
                            '''info = discord.Embed(title=f'Announcement!', color=0x992D22)
                            info.add_field(name="Title", value=mtitle, inline=False)
                            info.add_field(name="Content", value=body, inline=False)
                            info.add_field(name="Date", value=f'{datetime.now().strftime("%x")}', inline=False)
                            info.add_field(name="Time", value=f'{datetime.now().strftime("%X")}', inline=True)
                            info.add_field(name="For", value=forrole.name, inline=True)
                            info.add_field(name="By", value=author.mention, inline=True)'''
                            
                            info = discord.Embed(title=f'Announcement!', color=0x992D22)
                            info.add_field(name="Title", value=mtitle, inline=False)
                            info.set_thumbnail(url="https://da.gd/E1a13")
                            info.set_author(name=author.name, url=author.avatar_url, icon_url=author.avatar_url)
                            info.add_field(name="Content", value=body, inline=False)
                            info.set_footer(text=forrole.name, icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
                            info.add_field(name="Time", value=f'{datetime.now().strftime("%X")}', inline=True)
                            info.add_field(name="Date", value=f'{datetime.now().strftime("%x")}', inline=True)
                            await channel.send(embed=info)
                            
                        except Exception as e:
                            await ctx.author.send(e, delete_after=Delete_after_duration*100)
                            await ctx.send("Error: " + str(chan), delete_after=Delete_after_duration)
                except Exception as e:
                    await ctx.send(e, delete_after=Delete_after_duration)
            else:
                await ctx.send(f'You are not a Sudo User - {ctx.message.author.mention}', delete_after=Delete_after_duration)
        else:
            await ctx.send("No Sudo Users were found! Add them using .addsudo", delete_after=Delete_after_duration)
        return

    @commands.command(name='AddSudoUser', description='Add Sudo Users', aliases=['addsudo'], usage='.addsudo @username')
    async def addsudouser(self, ctx, member: discord.Member):
        print(Sudo_user)
        print(member.id)
        author = ctx.message.author
        await ctx.message.delete()
        print(author)
        if str(author.id) in Sudo_user or str(ctx.message.author) == 'Aayush#0923':
            msg = await ctx.send(
                f'{ctx.message.author} has requested that {member.mention} be added to Sudo User list!!')
            if member.id not in Sudo_user:
                Sudo_user.append(member.id)  # add memeber to Sudo_users
                await msg.edit(
                    content=f':ok: {member.mention} was added to Sudo User List as requested by {author.mention}')
            else:
                await msg.edit(content=f'{member.mention} was already a Sudo User...',delete_after=Delete_after_duration)
        else:
            await ctx.send(f'Unauthorized user - {author.mention}',delete_after=Delete_after_duration)

    @commands.command(name='RemoveSudoUser', description='Removes Sudo Users', aliases=['rmsudo'],
                      usage='.rmsudo @username')
    async def remsudouser(self, ctx, member: discord.Member):
        print(Sudo_user)
        print(member)
        author = ctx.message.author
        await ctx.message.delete()
        print(author)
        if str(author.id) in Sudo_user or str(ctx.message.author) == 'Aayush#0923':
            msg = await ctx.send(f'{ctx.message.author} has requested that {member} be removed from Sudo User list!!')
            if member.id in Sudo_user:
                Sudo_user.remove(member.id)  # add memeber to Sudo_users
                await msg.edit(content=f':ok: {member} was removed from Sudo User List as requested by {author}')
            else:
                await msg.edit(content=f'{member} was already a Sudo User...')
        else:
            await ctx.send(f'Unauthorized user - {author}', delete_after=Delete_after_duration)

    @commands.command(name='Add_Channel', description='Add channel to list',
                      aliases=['addann', 'announceadd', 'addchan'],
                      usage='.addchan <use this in channel you want to announce in>')
    async def addchanneltolist(self, ctx):
        print(f'channels : {channels}')
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.id in Sudo_user:  # does user have admin rights?
            ad_ch = ctx.message.channel.id  # get channel id
            await ctx.message.delete()

            if ad_ch in channels:
                await ctx.send('Already in update list', delete_after=Delete_after_duration)
            else:
                channels.append(ad_ch)
                print(f'{ctx.message.channel.name} was added.')
                await ctx.send('Channel added!',delete_after=Delete_after_duration)
        else:
            await ctx.send('Unauthorized User',delete_after=Delete_after_duration)
        return

    @commands.command(name='Remove', description='Removes a channel from announce list', aliases=['rmchan'],
                      usage='.rmchan <use this in the channel you want to remove from announcement list>')
    async def removechannelfromlist(self, ctx):
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.id in Sudo_user:
            re_ch = ctx.message.channel.id
            await ctx.message.delete()
            try:
                if re_ch in channels:
                    channels.remove(re_ch)
                    await ctx.send(f'Channel {ctx.message.channel.name} was removed.', delete_after=Delete_after_duration)
                else:
                    await ctx.send(f'Channel {ctx.message.channel.name} was not found in list.',delete_after=Delete_after_duration)
            except:
                await ctx.send('Error occured while remove the channel.',delete_after=Delete_after_duration)
        else:
            await ctx.send('Unauthorized User - :no_entry:',delete_after=Delete_after_duration)

    @commands.command(name='listsudousers', description='Lists all the existing sudo users',
                      aliases=['lsuser', 'sudols', 'lssudo'],
                      breif='.lsuser|.sudols|.lssudo to get a list of Sudo Users')
    async def listsudousers(self, ctx):
        await ctx.message.delete()
        if len(Sudo_user) > 0:
            msg = ''
            c = 0
            for i in Sudo_user:
                user = discord.utils.get(ctx.guild.members, id=i)
                if user:
                    c += 1
                    msg += f'{c}. {user}\n'
            await ctx.send(f'Found {c} users as Sudo Users \n {msg}\n\nThis message is scheduled to be destroyed in {Delete_after_duration*10}sec. ', delete_after=Delete_after_duration*10)
        else:
            await ctx.send(f'Populate the Sudo User list first. Use .addsudo <@member_name>', delete_after=Delete_after_duration)

    @commands.command(name='listchannels', description='Lists all the existing announcement chats', aliases=['lschan'],
                      usage='.lschan <to get a list of available announcement channels>')
    async def listchannels(self, ctx):
        await ctx.message.delete()
        if len(channels) > 0:
            msg = ''
            c = 0
            for i in channels:
                c += 1
                msg += f'{c}. {str(i)}'
            await ctx.send(f'Found {c} channels in Announcement List with ids:\n{msg} \n\nThis message is scheduled to be destroyed in {Delete_after_duration*10}sec.', delete_after=Delete_after_duration*10)
        else:
            await ctx.send(f'Channel list empty.', delete_after=Delete_after_duration)


def setup(client):
    client.add_cog(Announce(client))
