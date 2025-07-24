import os
import asyncio
from threading import Thread
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import MessageMediaType

# 🔐 Environment variables (Set these in Replit Secrets)
API_ID = int(os.environ.get("API_ID", "123456"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

# 🤖 Initialize Pyrogram bot
app = Client("haklesh_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 🧠 User-specific memory
user_remove_words = {}     # {user_id: [word1, word2, ...]}
user_caption_store = {}    # {user_id: {"step": "waiting_caption",
