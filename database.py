import sqlite3

# 連接 SQLite
conn = sqlite3.connect("claude_context.db")
cursor = conn.cursor()

# 建立對話歷史記錄表
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT NOT NULL,
    ai_response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
conn.close()