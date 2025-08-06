# weather_server.py
import sys
import json
import time

# 一個簡單的工具函式
def get_weather(city: str):
    """根據城市名稱回報天氣"""
    # 為了範例簡單，我們直接回傳固定的天氣資訊
    return f"今天 {city} 的天氣是晴時多雲，氣溫攝氏 28 度。"

def main():
    # MCP 伺服器透過標準輸入/輸出來溝通
    # 這裡我們模擬一個簡單的請求-回應循環
    for line in sys.stdin:
        try:
            request = json.loads(line)
            
            # 檢查是否是工具調用的請求
            if request.get("method") == "tool_code" and request.get("params", {}).get("name") == "get_weather":
                city = request["params"]["args"].get("city", "未知地點")
                result = get_weather(city)
                
                # 建立並回傳 JSON-RPC 格式的回應
                response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id"),
                    "result": {
                        "tool_code_output": {
                            "output": result
                        }
                    }
                }
                sys.stdout.write(json.dumps(response) + '\n')
                sys.stdout.flush()

        except json.JSONDecodeError:
            # 忽略無法解析的行
            pass

if __name__ == "__main__":
    # 初始的握手訊息，向 Gemini CLI 宣告我們擁有的工具
    tool_definition = {
        "jsonrpc": "2.0",
        "method": "mcp.register",
        "params": {
            "tools": [{
                "function": {
                    "name": "get_weather",
                    "description": "取得指定城市的即時天氣資訊",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "description": "要查詢天氣的城市名稱，例如：台北、高雄"
                            }
                        },
                        "required": ["city"]
                    }
                }
            }]
        }
    }
    sys.stdout.write(json.dumps(tool_definition) + '\n')
    sys.stdout.flush()
    
    # 進入主循環，等待請求
    main()
