
import discord
from discord.ext import commands
import asyncio
from datetime import datetime
from PbBot import Delete_after_duration

channels = [708025328345415740, 707715073308753925]
Sudo_user = [259370246681395210, 645189639430340609]        # TODO: Implement database for such tasks

# TODO: Fix user mentions


class BetterAnnounce(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='Better Announcer',
                      description='# Don\'t tag roles directly for now.\nAnnouncer, but it asks for inputs like title and content seperately and multiword title is supported',
                      aliases=['bann'],
                      usage='.bann <timeout duration | default at 30secs>')
    async def betterinp(self, ctx: commands.Context, timeofout: int=30):
        async def takinginput(self, *ques: str):
            temp = await ctx.send(f'{ques}')
            try:
                resp = await self.client.wait_for('message', timeout=timeofout)       # add a check for image and other stuff
            except asyncio.TimeoutError:
                await temp.edit(content=f'Time out error!!!')
            else:
                print("else is broken")
                await temp.edit(content=f'Query : {ques}\n {resp.author.name} responded with ```{resp.content}```')
                return [resp.content, resp]
            return [None, None]
        original_message = ctx.message
        await original_message.delete()
        [ask_title, title_ctx] = await takinginput(self, "Please enter the title : ")
        [ask_content, content_ctx] = await takinginput(self, "Please send the content : ")
        [ask_role, role_ctx] = await takinginput(self, "Please send for role : ")           # TODO : Add ability to directly add roles
        author = original_message.author
        if len(Sudo_user) > 0:
            if author.id in Sudo_user:  # compare usernames
                # if True:
                await ctx.send('User auth - :ok:', delete_after=(Delete_after_duration / 2))
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
                            info = discord.Embed(title=f'Announcement!', color=0x992D22, )
                            info.add_field(name="Title", value=ask_title, inline=False)
                            info.set_thumbnail(url="https://da.gd/E1a13")
                            info.set_author(name=f'@{author.name}', url=author.avatar_url, icon_url=author.avatar_url)            # TODO: Fix author profile url
                            info.add_field(name="Content", value=ask_content, inline=False)
                            info.set_footer(text=ask_role,
                                            icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
                            info.add_field(name="Time", value=f'{datetime.now().strftime("%X")}', inline=True)
                            info.add_field(name="Date", value=f'{datetime.now().strftime("%x")}', inline=True)
                            await channel.send(embed=info)
                            await title_ctx.delete()
                            await content_ctx.delete()
                            await role_ctx.delete()
                        except Exception as e:
                            await ctx.author.send(e, delete_after=Delete_after_duration * 10)
                            await ctx.send("Error: " + str(chan), delete_after=Delete_after_duration)
                except Exception as e:
                    await ctx.send(e, delete_after=Delete_after_duration)
            else:
                await ctx.send(f'You are not a Sudo User - {ctx.message.author.mention}',
                               delete_after=Delete_after_duration)
        else:
            await ctx.send("No Sudo Users were found! Add them using .addsudo", delete_after=Delete_after_duration)
        return




def setup(client):
    client.add_cog(BetterAnnounce(client))
