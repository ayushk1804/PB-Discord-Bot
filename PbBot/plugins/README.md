### Formation of new plugins
Now I will show a short script to show the formation of the desired script.
```python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.command() #for commands
    # @commands.Cog.listener #for event listener


def setup(client):
    client.add_cog(Example(client))
```
