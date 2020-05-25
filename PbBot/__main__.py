#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780


from discord.ext import commands
import discord
import os
import time
from PbBot import (
    BOT_TOKEN,
    Delete_after_duration,
    LOG_CHANNEL_ID
    )
import logging
from datetime import datetime

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)        # CRITICAL, ERROR, WARNING, INFO, and DEBUG and if not specified defaults to WARNING
handler = logging.FileHandler(filename='./logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# TODO Maybe make a function for send and edit - Remove redundant code.

# for custom help command visit da.gd/VSjOf

if __name__ == "__main__":
    client = commands.Bot(command_prefix=commands.when_mentioned_or(','),
                          description='Testing is good!!.Find the Souce Code - https://github.com/ayushk780/PB-Discord-Bot. Submit your feature requests to @Aayush#0923.',
                          case_insensitive=True
                          )
    # await client.change_presence(status=discord.Status.online, activity=discord.Game('Prefix "." Use (.help)'))
    logger.info(f'Client prefix has been set to "."')
    
    @commands.has_role('Admin')
    @client.command(name='load',brief='Loads a new Plugin (only for admins)', description='Loads a new Plugin (only for admins)', usage='.load <plugin file name>' )
    async def load(ctx, extension):
        await ctx.message.delete()
        try:
            client.load_extension(f'PbBot.plugins.{extension}')
            await ctx.send(f'Plugin {extension} was loaded successfully.', delete_after=Delete_after_duration)
            logger.info(f'{extension} was loaded successfully')
        except:
            await ctx.send(f'Plugin {extension} could not be loaded, Please verify the Plugin name.', delete_after=Delete_after_duration)
            logger.exception(f'{extension} failed to load')

    @commands.has_role('Admin')
    @client.command(name='unload',brief='Unloads a Plugin (only for admins)', description='Unloads a plugin (only for admins)', usage='.unload <plugin file name>' )
    async def unload(ctx, extension):
        await ctx.message.delete()
        try:
            client.unload_extension(f'PbBot.plugins.{extension}')
            await ctx.send(f'Plugin {extension} was unloaded successfully.', delete_after=Delete_after_duration)
            logger.info(f'{extension} was unloaded successfully')
        except:
            await ctx.send(f'Plugin {extension} could not be unloaded, Please verify the Plugin name.', delete_after=Delete_after_duration)
            logger.exception(f'{extension} failed to unload')

    @commands.has_role('Admin')
    @client.command(name='reload',brief='Reloads a plugin (or all) (only for admins)', description='Reloads plugins (specific | all) (only for admins)', usage='.reload <allplugins | plugin file name>' )
    async def reload(ctx, extension: str = 'allplugins'):
        await ctx.message.delete()
        try:
            if extension == 'allplugins':
                count=0
                for plugins in os.listdir('./PbBot/plugins'):
                    if plugins.endswith('.py') and not plugins.startswith('_'):
                        try:
                            client.unload_extension(f'PbBot.plugins.{plugins[:-3]}')# an attempt to ignore private plugins
                            client.load_extension(f'PbBot.plugins.{plugins[:-3]}')  # remove .py from plugin name
                            count += 1
                        except:
                            logger.exception(f'{plugins[:-3]} failed to reload')
                ctx.send(f'Bot is online!\nReloaded {count} plugins',delete_after=Delete_after_duration)
                logger.info(f'Bot is online!\nReloaded {count} plugins')
            else:
                client.unload_extension(f'PbBot.plugins.{extension}')
                client.load_extension(f'PbBot.plugins.{extension}')
                await ctx.send(f'Plugin {extension} was reloaded successfully.', delete_after=Delete_after_duration)
                logger.info(f'{extension} was reloaded successfully')
        except:
            await ctx.send(f'Plugin {extension} could not be reloaded please verify the Plugin name.', delete_after=Delete_after_duration)
            logger.exception(f'{extension} failed to reload')


    @client.event
    async def on_ready():
        count = 0
        # botStartTime = time.time()
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Prefix "." Use (.help)'))
        logger.info('Logged in as '+client.user.name+' (ID:'+str(client.user.id)+') | Connected to '+str(len(client.guilds))+' servers')
        # client.remove_command('help')      # for when helper prettify will work
        for plugins in os.listdir('./PbBot/plugins'):
            if plugins.endswith('.py') and not plugins.startswith('_'):  # an attempt to ignore private plugins
                try:
                    client.load_extension(f'PbBot.plugins.{plugins[:-3]}')  # remove .py from plugin name
                    count += 1
                except:
                    logger.exception(f'{plugins[:-3]} failed to load during on_ready.')
        logger.info(f'Bot is online!\nLoaded {count} plugins')
        text_channel_list=[]
        for botguilds in client.guilds:
            for channel in botguilds.text_channels:
                if 'bot' in str(channel.name).lower():            # Change accordingly
                    text_channel_list.append(channel)
                    await channel.send(f'BOT ONLINE!!', delete_after=Delete_after_duration)
        print(f'Bot is online!\nLoaded {count} plugins')
        
        # chanel = discord.utils.get()
        # await channel.send(f'Bot was loaded successfully', delete_after=Delete_after_duration)


    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f'Hey Noob! {ctx.message.author.mention}. Go through the help menu first! Use {client.command_prefix}help', delete_after=Delete_after_duration)
            logger.info(f'Noob! {ctx.message.author.mention}, has used {ctx.message} command...')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Hey Noob! {ctx.message.author.mention} you have not provided sufficient arguments. Go through the help menu first! Use {client.command_prefix}help', delete_after=Delete_after_duration)
            logger.info(f'Noob! {ctx.message.author.mention}, has made a missing(bad) argument request in {ctx.message} command.')

        elif isinstance(error, commands.MissingPermission):
            await ctx.send(f'Hey Noob! {ctx.message.author.mention} bot doesnt have sufficient permissions for that. Go ask the admin.', delete_after=Delete_after_duration)
            logger.info(f'Noob! {ctx.message.author.mention}, bot was missing permission for {ctx.message} command.')
        else:
            await ctx.send(f'Hey Noob! {ctx.message.author.mention} you have triggered an unknown error. Go through the help menu first! Use {client.command_prefix}help', delete_after=Delete_after_duration)
            logger.exception(f'Noob! {ctx.message.author.mention} has triggered {error} and it was not yet handled.')
        await ctx.message.delete()

    @client.event
    async def on_guild_join(guild: discord.Guild):
        general = discord.utils.find(lambda x: x.name == 'general', guild.text_channels)
        channel = client.get_channel(708250449203167262)        #log channel id
        embed_join = discord.Embed(description=f'Joined server **{guild.name}** with **{len(guild.members)}** members | Total: **{len(client.guilds)}** servers', timestamp=datetime.utcnow(), colour=discord.Colour.green())
        await channel.send(embed=embed_join)
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(
                    description=f'Thanks for inviting me! | Use **{client.command_prefix}help** for more info on commands \n',
                    colour=discord.Colour.red()
                    )
            embed.add_field(name='Command Prefix', value='`. ` or `@mention`')
            embed.set_footer(text='Made by @Aayush#0923')
            await general.send(embed=embed)
    
    @client.event
    async def on_guild_remove(guild: discord.Guild):
        channel = client.get_channel(708250449203167262)
        embed_leave = discord.Embed(description=f'Left server **{guild.name}** with **{len(guild.members)}** members | Total: **{len(client.guilds)}** servers', timestamp=datetime.utcnow(), colour=discord.Colour.red())
        await channel.send(embed=embed_leave)
    
    
    client.run(BOT_TOKEN)
