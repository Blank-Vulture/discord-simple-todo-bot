# Simple ToDo Discord Bot（日本語 README）

このボットは、外部サーバーを一切使用せず、Discordのテキストチャンネルを「ToDoリストのデータベース」として活用するPython製のシンプルなボットです。

## ✅ 特徴

- 外部データベース不要（Discordチャンネルをデータ保存に使用）
- `!add`, `!list`, `!done` の簡単操作
- DiscordDatabaseライブラリで簡易的なキー・バリューストアを実現

---

## 🔧 セットアップ手順

### 1. Discord Developer Portalでアプリ作成

1. https://discord.com/developers/applications にアクセス
2. 「New Application」から「Simple ToDo Manager」を作成
3. 「Bot」セクションで「Add Bot」→「Message Content Intent」を有効化
4. 「TOKEN」をコピーして `token.txt` に保存
5. ボットを追加したいサーバのIDを `guild.txt` に保存（右クリック → サーバーIDをコピー）

### 2. 必要なライブラリをインストール

```bash
pip install discord.py DiscordDatabase
```

### 3. ディレクトリ構成

```
project/
├── bot.py
├── token.txt   # ボットトークン（1行）
├── guild.txt   # ギルドID（1行）
```

### 4. `bot.py` の起動

```bash
python3 bot.py
```

---

## ⚙️ systemd サービスとして起動（Linux）

1. `/etc/systemd/system/todo-bot.service` を以下のように作成：

```ini
[Unit]
Description=Simple ToDo Discord Bot
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME/discord-bot
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/discord-bot/bot.py
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

2. サービス有効化と起動：

```bash
sudo systemctl daemon-reload
sudo systemctl enable todo-bot
sudo systemctl start todo-bot
```

---

## 📝 コマンド一覧

| コマンド              | 説明                       |
|-----------------------|----------------------------|
| `!add タスク内容`     | タスクを追加する           |
| `!list`               | 登録されたタスク一覧を表示 |
| `!done タスク内容`    | タスクを完了（削除）       |

---

## 📌 注意点

- チャンネルが自動生成されない場合は、ボットに「チャンネルの管理」権限があるか確認
- データはDiscordチャンネルに保存されるため、**チャンネルの非公開化を推奨**

---

## 🐍 対応バージョン

- Python 3.8以降
- discord.py v2.x
- DiscordDatabase 最新版

---

## 📄 ライセンス

MIT
