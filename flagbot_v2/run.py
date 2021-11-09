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
    if isinstance(error, commands.CommandNotFound):
        embed.add_field(name="Command Not Found", value="올바른 명령어를 입력해주세요 ㅜ^ㅜ")
    await ctx.send(embed=embed)

@app.command()
async def help(ctx):
    if channel_check(ctx.channel.id) != False:
        e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
        e.add_field(name="!calendar", value="POX 2021 대회 시작과 종료 일정을 알려줘요!", inline=False)
        e.add_field(name="!flag1", value="플래그 주세요 #1", inline=False)
        e.add_field(name="!flag2", value="플래그 주세요 #2", inline=False)
        e.set_footer(text="CopyRight Demon TEAM & SISS")
        await ctx.send(embed=e)
    else:
        await ctx.send("명령어를 사용할 수 없는 채널입니다. #flag봇 채널을 사용해주세요.")

@app.command()
async def calendar(ctx):
    if channel_check(ctx.channel.id) != False:
        e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
        e.add_field(name="일정 안내", value="POX 2021 " + "\n " + "Start : 2021/11/11 (AM) 11:11 " + "\n" + "End : 2021/11/11 (PM) 11:11", inline=False)
        e.set_footer(text="CopyRight Demon TEAM & SISS")
        await ctx.send(embed=e)
    else:
        await ctx.send("명령어를 사용할 수 없는 채널입니다. #flag봇 채널을 사용해주세요.")    

@app.command()
async def flag1(ctx):
    if channel_check(ctx.channel.id) != False:
        e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0x1d87d7)
        e.add_field(name="플래그 주세요 #1", value=flag_1, inline=False)
        e.set_footer(text="CopyRight Demon TEAM & SISS")
        await ctx.author.send(embed=e)
    else:
        await ctx.send("명령어를 사용할 수 없는 채널입니다. #flag봇 채널을 사용해주세요.")

@app.command()
async def flag2(ctx):
    try:
        if channel_check(ctx.channel.id) != False:
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
        else:
            await ctx.send("명령어를 사용할 수 없는 채널입니다. #flag봇 채널을 사용해주세요.")
    
    except AttributeError:
        e = Embed(title="POX 2021", url="https://ctf.powerofxx.org", description="안녕하세요! POX 2021 도우미 입니다.", color=0xff0000)
        e.add_field(name="오류!", value="인증되지 않은 사용자 입니다.", inline=False)
        e.set_footer(text="CopyRight Demon TEAM & SISS")
        await ctx.author.send(embed=e)

if __name__ == "__main__":
    app.run(token_load())