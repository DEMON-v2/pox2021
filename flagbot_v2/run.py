from discord.ext import commands
from discord import Embed, Game, Status
from discord.utils import get
from utils import token_load, channel_check

app = commands.Bot(command_prefix='!')
app.remove_command('help')

flag_1 = "POX{th3s_is_d1sc0rd"
flag_2 = "_cl3ent_b0t_f@ag#}"

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
    e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
    e.add_field(name="!calendar", value="POX 2021 대회 시작과 종료 일정을 알려줘요!", inline=False)
    e.add_field(name="!flag1", value="플래그 주세요 #1", inline=False)
    e.add_field(name="!flag2", value="플래그 주세요 #2", inline=False)
    e.add_field(name="!verify", value="사용자 권한을 확인합니다.", inline=False)
    e.set_footer(text="CopyRight Demon TEAM & SISS")
    await ctx.send(embed=e)

@app.command()
async def calendar(ctx):
    e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
    e.add_field(name="일정 안내", value="POX 2021 " + "\n " + "Start : 2021/11/11 (AM) 11:11 " + "\n" + "End : 2021/11/11 (PM) 11:11", inline=False)
    e.set_footer(text="CopyRight Demon TEAM & SISS")
    await ctx.send(embed=e)  

@app.command()
async def flag1(ctx):
    e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
    e.add_field(name="플래그 주세요 #1", value=flag_1, inline=False)
    e.set_footer(text="CopyRight Demon TEAM & SISS")
    await ctx.author.send(embed=e)

@app.command()
async def flag2(ctx):
    try:
        organizer = get(ctx.guild.roles, name="Organizer")
        if organizer in ctx.author.roles:
            e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
            e.add_field(name="플래그 주세요 #2", value=flag_2, inline=False)
            e.set_footer(text="CopyRight Demon TEAM & SISS")
        else:
            e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0xff0000)
            e.add_field(name="오류!", value="인증되지 않은 사용자 입니다.", inline=False)
            e.set_footer(text="CopyRight Demon TEAM & SISS")
            await ctx.author.send(embed=e)
    
    except AttributeError:
        e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0xff0000)
        e.add_field(name="오류!", value="인증되지 않은 사용자 입니다.", inline=False)
        e.set_footer(text="CopyRight Demon TEAM & SISS")
        await ctx.author.send(embed=e)

@app.command()
async def verify(ctx):
    organizer = get(ctx.guild.roles, name="Organizer")
    if organizer in ctx.author.roles:
        e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
        e.add_field(name="Check Permission", value=str(ctx.author) + " 님은 관리자입니다.", inline=False)
        e.set_footer(text="CopyRight Demon TEAM & SISS")
        await ctx.send(embed=e)
    else:
        e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0xff0000)
        e.add_field(name="오류!", value=str(ctx.author) + " 님은 인증되지 않은 사용자 입니다. (your not Organizer permission)", inline=False)
        e.set_footer(text="CopyRight Demon TEAM & SISS")
        await ctx.send(embed=e)

if __name__ == "__main__":
    app.run(token_load())