import discord
from discord.ext import commands
import random
import datetime
import praw

bot = commands.Bot(command_prefix='!')
reddit = praw.Reddit(client_id='2VsRbv8osilKPA',
                     client_secret='nSFhb7SY6NQpfRUr_p4tFecaGsE',
                     user_agent='wohlf_script')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='with you!'))
    print('------')
    print("Logged in to:")
    for server in bot.servers:
        print(server)
    print('------')
    print('Ready for commands.')

# Utility commands


@bot.command()
async def math(left: int, operation: str, right: int):
    """Perform basic math on two numbers."""
    if operation == "+":
        total = right + left
    elif operation == "-":
        total = right - left
    elif operation == "*":
        total = right * left
    elif operation == "/":
        total = right / left
    else:
        total = "Sorry, I didn't understand your math. The format is x + y or x*y, supported operations are +, -, *, /"
    await bot.say(total)


@bot.command()
async def roll(dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except ValueError:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)


@bot.command()
async def choose(*choices: str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

# Public message based commands / events


@bot.command(pass_context=True)
async def stfu(ctx):
    """Tells someone to stfu"""
    if ctx.message.mentions:
        for mention in ctx.message.mentions:
            await bot.say('Shut the FUCK up {0.mention}'.format(mention))


@bot.command(pass_context=True)
async def pet(ctx):
    """Pets someone."""
    if ctx.message.mentions:
        for mention in ctx.message.mentions:
            await bot.say('*pets* {0.mention}'.format(mention))


"""
@bot.event
async def on_message_delete(message):
    fmt = '{0.author.name} has deleted the message:\n{0.content}'

    def is_me(m):
        return m.author == bot.user
    if not is_me(message):
        await bot.send_message(message.channel, fmt.format(message))
"""


@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await bot.say(server, fmt.format(member, server))


@bot.command(pass_context=True)
async def nite(ctx):
    '''Says good night to you."'''
    choices = ['Good night', 'Nini', 'Gnight', 'Nite', 'Sweet dreams', 'Sleep well',
               'Don\'t let the bed bugs bite', 'See you tomorrow']
    await bot.say('{}, {}'.format(random.choice(choices), ctx.message.author.mention))


@bot.command()
async def anikin():
    '''Quotes the greatest character from George Lucas' magnum opus.'''
    choices = ['I HATE YOU!',
               "Don't lecture me, Obi-Wan! I see through the lies of the Jedi. I do not fear the dark side as you do.",
               "I have brought peace, freedom, justice, and security to my new Empire.",
               "If you're not with me, then you're my enemy.",
               "Master Skywalker, there are too many of them. What are we going to do? *light saber noise*",
               "From my point of view, the Jedi are evil!"]
    await bot.say(random.choice(choices))


@bot.command()
async def maymay():
    """Posts a dank maymay."""
    maymays = []
    for submission in reddit.subreddit('dankmemes').hot(limit=10):
        if submission.shortlink:
            maymays += submission.shortlink

    await bot.say(maymays[random.randint(0, 9)])


# Dangerous commands that actually do shit on the server

@bot.command(pass_context=True)
async def delet(ctx):
    '''Deletes recent messages from bot.'''
    def is_me(m):
        return m.author == bot.user

    deleted = await bot.purge_from(ctx.message.channel, limit=100, check=is_me, around=datetime.datetime.utcnow())
    await bot.send_message(ctx.message.channel, 'Deleted {} message(s)'.format(len(deleted)))


@bot.command(pass_context=True)
async def delet_this(ctx):
    """Deletes recent messages from mentioned users"""
    def is_user(m):
        return m.author == ctx.message.mentions[0]

    deleted = await bot.purge_from(ctx.message.channel, limit=100, check=is_user,
                                   around=datetime.datetime.utcnow())
    await bot.send_message(ctx.message.channel, 'Deleted {} message(s)'.format(len(deleted)))


bot.run('MjYzNzUyMDYxMzk5NzI4MTI4.C0Wlwg.oR0mnFkSBwSJtAlKkBNbR6qp_x0')
