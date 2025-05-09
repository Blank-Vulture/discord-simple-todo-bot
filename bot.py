import discord
from discord.ext import commands
import aiosqlite

# 外部ファイルからTOKENとGUILD_IDを読み込む
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

with open("guild.txt", "r") as f:
    DB_GUILD_ID = int(f.read().strip())

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # データベースの初期化
    async with aiosqlite.connect("tasks.db") as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)"
        )
        await db.commit()
    print(f"Logged in as {bot.user}")

@bot.command()
async def add(ctx, *, task):
    async with aiosqlite.connect("tasks.db") as db:
        await db.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        await db.commit()
    await ctx.send(f"タスクを追加しました: {task}")

@bot.command()
async def list(ctx):
    async with aiosqlite.connect("tasks.db") as db:
        async with db.execute("SELECT id, task FROM tasks") as cursor:
            rows = await cursor.fetchall()
    if rows:
        task_list = "\n".join(f"{index + 1}. {row[1]}" for index, row in enumerate(rows))
        await ctx.send(f"現在のタスク:\n{task_list}")
    else:
        await ctx.send("現在、タスクはありません。")

#!done, tasks.dbはsqlite
@bot.command()
async def done(ctx, task_name: str):
    try:
        async with aiosqlite.connect("tasks.db") as db:
            await db.execute("DELETE FROM tasks WHERE task = ?", (task_name,))
            await db.commit()
        # 例外処理を追加
        await ctx.send(f"タスクを完了しました: {task_name}")
    except Exception as e:
        await ctx.send(f"タスクの完了に失敗しました: {task_name}\nエラー: {e}")


#!clear
@bot.command()
async def clear(ctx):
    async with aiosqlite.connect("tasks.db") as db:
        await db.execute("DELETE FROM tasks")
        await db.commit()
    await ctx.send("全てのタスクを削除しました。")

bot.run(TOKEN)