# Discord TODO管理ボット

## 📌 概要

このDiscordボットは、SQLiteデータベースを使って、シンプルにタスクの追加・一覧表示・削除ができる日本語対応のTODO管理ボットです。

## ⚙️ 必要条件

- Python 3.8以上
- `discord.py`
- `aiosqlite`

## 🛠️ セットアップ手順

### 1. ライブラリのインストール

```bash
pip install discord.py aiosqlite
```

### 2. ファイルの準備

ルートディレクトリに以下のファイルを用意してください：

- `token.txt`：1行でDiscordボットのトークンを記載
- `guild.txt`：1行でGuild ID（サーバID）を記載

### 3. 実行

以下のコマンドで起動：

```bash
python bot.py
```

---

## 🚀 使い方

| コマンド | 機能 |
|---------|------|
| `!add タスク名` | タスクを追加 |
| `!list` | 現在のタスクを一覧表示 |
| `!done タスク名` | 指定したタスクを削除 |
| `!clear` | 全てのタスクを削除 |

---

## 💾 データ構造

タスクは `tasks.db` というSQLiteファイルに格納されます。起動時に自動生成されます。

```sql
CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task TEXT
);
```

---

## 📌 注意点

- `!done` は完全一致でタスク名を検索します。
- 同名タスクが複数ある場合、すべて削除されます。
- IDの詰め直しは行わず、表示時に連番で見せています。

---

## 🪪 ライセンス

MIT
