import discord
from discord.ext import commands
from DiscordDatabase import DiscordDatabase

# 外部ファイルからTOKENとGUILD_IDを読み込む
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

with open("guild.txt", "r") as f:
    DB_GUILD_ID = int(f.read().strip())

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
db = DiscordDatabase(bot, DB_GUILD_ID)
database = None

@bot.event
async def on_ready():
    global database
    database = await db.new("管理カテゴリ", "TODO管理チャンネル")
    print(f"Logged in as {bot.user}")

@bot.command()
async def add(ctx, *, task):
    await database.set(task, "未完了")
    await ctx.send(f"タスク「{task}」を追加しました。")

@bot.command()
async def list(ctx):
    tasks = await database.keys()
    if tasks:
        task_list = "\n".join(f"- {task}" for task in tasks)
        await ctx.send(f"現在のタスク:\n{task_list}")
    else:
        await ctx.send("現在、タスクはありません。")

@bot.command()
async def done(ctx, *, task):
    if await database.get(task):
        await database.delete(task)
        await ctx.send(f"タスク「{task}」を完了として削除しました。")
    else:
        await ctx.send(f"タスク「{task}」が見つかりませんでした。")

bot.run(TOKEN)