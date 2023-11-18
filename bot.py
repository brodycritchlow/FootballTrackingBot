from cogs.consts import BOT_TOKEN
import os
import discord

class Client(discord.Bot):
    async def on_ready(self):
        print('---------------------')     
        print('Logged in as:')
        print(f"{self.user.name=}")
        print(f"{self.user.id=}")
        print('---------------------')           

client = Client() 

for cog in os.listdir('cogs'):
    if cog.endswith('.py'): 
        client.load_extension(f'cogs.{cog[:-3]}')
        print(f"Loaded cog cogs.{cog[:-3]}")

if __name__ == "__main__":
    client.run(BOT_TOKEN)