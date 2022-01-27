import discord
import asyncio
import json
import random
import os
from Wordle import Wordle
from Users import *

print(os.getcwd())

class DiscordClient(discord.Client):

    async def on_ready(self):
        print(f"Ready as {self.user.id}")

    async def on_message(self, message):
    
        if (message.author.id == self.user.id):
            return

        user = Users.get_user(message.author.ID)
        message.content = message.content.lower()

        if (message.content == "$w" or message.content == "$wordle"):
            self.WordleObj = Wordle()
            self.WordleObj.setupWordleGame()
            user.gameActive = True
            await message.channel.send("guess a 5 letter word")

        if (message.content.startswith("$g") or message.content.startswith("$guess")) and self.flag:
            result = self.WordleObj.wordleGame(message.content)
            if result == [9, 9, 9, 9, 9]:
                await message.channel.send("try again, invalid input")
            elif result == [8, 8, 8, 8, 8]:
                await message.channel.send("ran out of guesses")
            else:
                botMessage = self.WordleObj.convertNumbersToSymbols(result)
                await message.channel.send(botMessage)
            
client = DiscordClient()
with open('config.json') as config_file:
    config = json.load(config_file)
client.run(config["TOKEN"])
            