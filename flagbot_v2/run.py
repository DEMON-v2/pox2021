from discord.ext import commands
from discord.ext.commands.errors import MissingRole
from discord.ext.commands.core import has_role
from discord import Embed, Game, Status
from discord.utils import get
from utils import token_load

app = commands.Bot(command_prefix='!')
app.remove_command('help')

@app.event
async def on_ready():
    await app.change_presence(status=Status.online, activity=Game('POX 2021 Help Bot'))

@app.event
async def on_command_error(ctx, error):
    embed = Embed(title="Error!", color=0xff0000)
    print(error)
    if isinstance(error, commands.CommandNotFound):
        embed.add_field(name="Command Not Found", value="올바른 명령어를 입력해주세요 ㅜ^ㅜ")
    await ctx.send(embed=embed)
    

@app.command()
async def help(ctx):
    e = Embed(title="Help Dask", description="!flag1 : Give me the Flag 1/2" + "\n" +
    "flag2 : Give me the Flag 2/2")
    await ctx.send(embed=e)

@app.command()
async def flag1(ctx):
    e = Embed(title="Give me the Flag #1", description="POX{th3s_is_d1sc0rd", color=0xCEFBC9)
    await ctx.author.send(embed=e)

@app.command()
async def flag2(ctx):
    try:
        organizer = get(ctx.guild.roles, name="Organizer")
        if organizer in ctx.author.roles:
            e = Embed(title="Give me the Flag #2", description="_cl3ent_b0t_f@ag#}", color=0xCEFBC9)
            await ctx.author.send(embed=e)
        else:
            e = Embed(title="UnAuthorized", description="UnAuthorized", color=0xff0000)
            await ctx.author.send(embed=e)
    except AttributeError:
        e = Embed(title="UnAuthorized", description="UnAuthorized", color=0xff0000)
        await ctx.author.send(embed=e)

if __name__ == "__main__":
    app.run(token_load())