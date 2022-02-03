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

        user = Users.get_user(message.author)
        message.content = message.content.lower()

        if (message.content == "$w" or message.content == "$wordle"):
            self.WordleObj = Wordle()
            self.WordleObj.setupWordleGame()
            user.gameActive = True
            embed=discord.Embed(title=f"{user.guessCount}/6", description= "guess a 5 letter word", color=0xcb1a1a)
            embed.set_author(name=f"{user.name}'s game")
            botMessage = await message.channel.send(embed=embed)
            user.activeGameKey = botMessage

        if (message.content.startswith("$g") or message.content.startswith("$guess")) and user.gameActive:
            result = self.WordleObj.wordleGame(message.content, user)
            if result == [9, 9, 9, 9, 9]:
                await message.channel.send("try again, invalid input")
            user.guessArray.append(result)
            if result == [8, 8, 8, 8, 8]:
                await message.channel.send("ran out of guesses")
            else:
                botMessage = self.WordleObj.convertNumbersToSymbols(user)
                embed=discord.Embed(title=f"{user.guessCount}/6", description= botMessage, color=0xcb1a1a)
                embed.set_author(name=f"{user.name}'s game")
                await user.activeGameKey.edit(embed=embed)
            
client = DiscordClient()
with open('config.json') as config_file:
    config = json.load(config_file)
client.run(config["TOKEN"])
            