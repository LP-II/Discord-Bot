import discord
from discord.ext import commands
import random 
client = commands.Bot(command_prefix = ".")

@client.event                                       # Funktion / Event
async def on_ready():
    print("Botten er klar til brug.")

@client.event
async def on_member_join(member):
    print(f"{member} har joinet serveren.")

@client.event
async def on_member_remove(member):
    print(f"{member} har forladt serveren.")

@client.command()                                     # Command
async def ping(ctx):
    await ctx.send(f"din ping er {round(client.latency * 1000)}ms")

@client.command(aliases=["spåkugle"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f"Spørgsmål: {question}\nSvar: {random.choice(responses)}")

client.run("NzQ3OTU5ODE3NjY2MDM1Nzky.X0Wd3A.xTz-oqjaEju7OEc41Q-lJvCvqDc")
