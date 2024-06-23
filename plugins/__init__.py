from aiohttp import web
from .route import routes
import re
import asyncio
import logging  
from pyrogram import Client, errors
from motor.motor_asyncio import AsyncIOMotorClient
from info import COLLECTION_NAME, LOG_CHANNEL, DATABASE_NAME, DATABASE_URI, GRP_LNK
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

 
