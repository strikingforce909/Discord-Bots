import discord
from discord.ext import commands, tasks

import os
import sqlite3

import time
import random

TOKEN = open("TOKEEN.txt", "r").read()

# opens the folder
BOT_PREFIX = ['=', '>', '<'] # command prompts; they operate the same.
dir_cugo = 'G:\Artrix-botz\PhysixsFun\cugo' # pathway to cugo folder.
bot = commands.Bot(command_prefix=BOT_PREFIX) # part commands.Bot() is a function in Discord API library; commands.Bot(command_prefix=BOT_PREFIX) is analigous to having a binder where command_prefix=BOT_PREFIX is like a piece of paper in the seciotn *.Bot and commands.Bot is the binder.
bot.remove_command('help') # bot.remove_command() is a function in Discord API library
"""
@tasks.loop(seconds=5)
asnyc def chng_pr(self):
    pass
"""


# THIS OPENS THE COGS
for filename in os.listdir(dir_cugo): # dir_cugo is G:\Artrix-botz\PhysixsFun\cugo; os is the library for file manipulation in Python.
    if filename.endswith('.py'): # filename.endswith('.py') is an os command view any file extentsion.
        bot.load_extension(f"cugo.{filename[:-3]}")
        print('Cog Has Loaded Succsesfully :)')

@bot.event # @variablename.event is a section inside bot which is part of the dicord library.
async def on_ready():
    db = sqlite3.connect('users.sqlite')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usr(user_id TEXT, selected TEXT, total TEXT, coins TEXT, redeems TEXT, mons TEXT)')
    print(discord.__version__)
    print("Logged in as: " + bot.user.name + "\n" "_____________________________")
    print(BOT_PREFIX)


@bot.command(pass_context=True, aliases=['physixsfun'])
async def prefix(ctx):
    thonka = random.choice(BOT_PREFIX)
    await ctx.send(f'My prefixs are `{BOT_PREFIX}!`')

    time.sleep(1.25)

    culorz = [0x9750C7, 0x000066, 0xA200FF, 0x0008FF]
    embed = discord.Embed(color=random.choice(culorz), timestamp=ctx.message.created_at, title='Need help!?', description=f'Dont worry I got you! \n Use {thonka}help to see all my commands :D!')

    embed.set_author(name=f"Help! - {ctx.author}", icon_url=bot.user.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def shutdown(ctx):
    if ctx.message.author.id == 361628174842593280:
        await ctx.send('Shuting Down')
        await bot.logout()
    else:
        await ctx.send('You arent a admin for this bot')



bot.run(TOKEN)

# First idea is Krypto, and Crypt. The guardian twins guarding Adatrass,
# the legendary ultimante Phsysixmon. NONONO lets go with the storyline k artrix?

# You fall down and once you open your eyes poof! Your uncle sits there staring at you.
# "Look, (@user) I know you've been waiting so long..choose your Phsysixmon now."
# *your uncle gives you a Phsysidex and  throws out a few Terraballs*
# *Phsysidex speaks* "Briteon, the white light fox Phsysixmon"
# "Aureon, the moonburst fossil fox Phsysixmon"
# "WuDo, the fighting fennec fox Phsysixmon that was redescovered after extinction."
# "Rippitrok, the waterfire nine tailed fox Phsysixmon."
# *You shrug* "Ye, ye..but which one?"
# "I could tell you all about those starters and there history if you want."
# "So. want me to tell you are not?" (pick yes or no)
# (if the person picked yes then ill tell u about it but if they said no..dont do anything ill think about that.)
# "Briteon is close to the pokemon family but is still apart of the PHSYSIXMON!"
# "Briteon has a long history, it evolved from light rats, the extinct beings we've been trying to bring back."
# "Briteon is special, for also its adams are formed from light."
# "Aureon, a unique fossil fox that was brung back to life by science."
# "It was discovered that it had weird powers, we call it a moon-shifter, some people call it a shape-shifter!"
# "For now, us humans think we're safe, scientists have looked and by their experiments.. they say that Aureon was made from moon adams. Specifally, the crescent star moon adam."
# *you slam the table* "UNCLE! Can't you just help me choose!?
# *your uncle chattered his teeth and said* "Ok (@user), CHOOSE YOUR PHSYSIXMON!"
# (There should be reactions to choose from and the bot edits the message and it shows what the reactions are)