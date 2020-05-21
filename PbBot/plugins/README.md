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
---

## Re/Un/Loading a new Plugin
> Use re/un/load command to test a new Plugin. These are defined when the bot starts.
```js
<server-prefix>load <plugin name>
<server-prefix>unload <plugin name>
<server-prefix>reload <plugin name>    (no arguments would result in reloading all plugins)
```
