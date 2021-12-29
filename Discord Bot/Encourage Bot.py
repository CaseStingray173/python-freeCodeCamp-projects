import discord
import requests
import json
import random
from replit import db
# from pyrandmeme import *
# from dadjokes import Dadjoke

client = discord.Client()

sad_words = ["sad",
             "depressed",
             "unhappy"]
saved_encouragements = ["Cheer Up!",
                        "Hang in there.",
                        "You are doing great",
                        "Love yourself"]


# Gets a random positive quote when a member requests in the chat
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return quote


def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]


def delete_encouragments(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


# def get_joke():
#     dad_joke = Dadjoke()
#     return dad_joke.joke


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.get_channel(856712241814044675).send("{0.user} is online".format(client))


# NOTE: ALL COMMANDS FOR THE BOT STARTS WITH $
@client.event
async def on_message(message):
    # If the user is the bot itself it does nothing
    if message.author == client.user:
        return

    # Checks if any other user type in Hello/hello
    # and then the bot responds with Hello
    hello = "HELLO"
    msg = message.content
    if msg.startswith(">" + hello.lower()):
        await message.channel.send("Hello!")

    if msg.startswith(">inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    options = saved_encouragements
    if "encouragements" in db.keys():
        options = options + db["encouragements"][:]

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith(">new"):
        encouraging_message = msg.split(">new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouragement added")

    if msg.startswith("$del"):
      encouragements = []
      if "encouragements" in db.keys():
        index = int(msg.split("$del",1)[1])
        delete_encouragments(index)
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)


    # if message.content.startswith(">meme"):
    #     meme = pyrandmeme()
    #     await message.channel.send(embed=await meme)
    #
    # if message.content.startswith(">joke"):
    #     joke = get_joke()
    #     await message.channel.send(joke)

client.run("ODU2NzE0OTY5MzQwNzA2ODE2.YNFD_Q.g9_wsumoH5feE3f_2gQLXFtGtUY")
