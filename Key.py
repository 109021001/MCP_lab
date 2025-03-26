import anthropic
import sqlite3
import os

# 設定 API Key
ANTHROPIC_API_KEY = "你的_API_Key"

# 初始化 Claude API
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# 連接 SQLite 資料庫
def save_to_database(user_input, ai_response):
    conn = sqlite3.connect("claude_context.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user_input, ai_response) VALUES (?, ?)", 
                   (user_input, ai_response))
    conn.commit()
    conn.close()

# 呼叫 Claude API
def chat_with_claude(user_message):
    response = client.messages.create(
        model="claude-3-opus-20240229",  # 請根據你的方案選擇正確的 Claude 版本
        max_tokens=100,
        messages=[{"role": "user", "content": user_message}]
    )
    
    ai_response = response.content[0].text  # 取得 Claude 回應
    save_to_database(user_message, ai_response)  # 儲存對話
    return ai_response

# 測試聊天
user_input = "Hello, Claude! What can you do?"
ai_output = chat_with_claude(user_input)
print("Claude 回應:", ai_output)
