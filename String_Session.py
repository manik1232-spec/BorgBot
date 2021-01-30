#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")
APP_ID = int(input("Enter APP ID here:1529663 "))
API_HASH = input("Enter API HASH here: f5d41be7527184d35c2db90c91094f29")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
