"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "27149454"))
API_HASH = getenv("API_HASH", "044ef37e1a567101317e08c34b04ccd3")
BOT_TOKEN = getenv("BOT_TOKEN", "6628443454:AAHsM9wW6zg0uTkxsNMzVYidSG3hRbdnrL8")
SESSION_STRING = getenv("SESSION_STRING", "BQADLuNeFdTFELBDiwER3gz935Y5XjPV-sREjiQFz9GJspSG_28ntQIg91ZpdCKxtSoC86lOFQxfeLaG7X8jENlJin3OdE3_U1LvLNiNFlCvulb-KUYxY68cHX9b63Kde2w--aoJhnk8m9OFcg9Qt_71bwgoRhCZuTYraI09E8BFMSgH2f2HW7wHsN8gxL0pLZAFGE7MiFqCgwN_vVwntMaLg1iErPxzlUbbaf6G7r7Ql8yNPtPYHMH0HfJBfn0vOcwnNdwIQNfm6MLbLm0lfsxdyY1BJp-njIF2QWsOD2L0PaTcroy-c6eLsu0cERNPQRaqscrHDfucm3xYelVlPSZaAAAAAURkLLoA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AsmSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
