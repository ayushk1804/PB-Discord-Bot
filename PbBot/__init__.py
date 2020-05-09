#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Aayush Kumar - @ayushk780

import os
import time

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from PbBot.sample_config import Config
else:
    from config import Config

botStartTime = time.time()

# TODO: is there a better way?

BOT_TOKEN = Config.BOT_TOKEN
AUTH_CHANNEL = Config.AUTH_CHANNEL
Delete_after_duration = Config.Delete_after_duration
LOG_CHANNEL_ID = Config.LOG_CHANNEL_ID
