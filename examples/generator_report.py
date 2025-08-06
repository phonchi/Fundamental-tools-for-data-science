# generate_report.py
import pandas as pd
import sys
import os
from datetime import datetime

def generate_html_report(df, input_filename):
    """
    根據提供的 DataFrame 生成 HTML 報告的字串。
    """
    # 將 DataFrame 轉換為 HTML 表格
    head_html = df.head().to_html(classes='table table-striped', border=0)
    describe_html = df.describe().to_html(classes='table table-striped', border=0)
    
    # 取得目前時間
    generation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # HTML 模板
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>資料分析報告: {os.path.basename(input_filename)}</title>
        <style>
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 960px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                background-color: #fff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            h1, h2 {{
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }}
            .table-container {{
                overflow-x: auto;
                margin-top: 20px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #3498db;
                color: #fff;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            footer {{
                text-align: center;
                margin-top: 30px;
                font-size: 0.9em;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>資料分析報告</h1>
            <p><strong>來源檔案:</strong> {os.path.basename(input_filename)}</p>
            
            <h2>資料預覽 (前 5 筆)</h2>
            <div class="table-container">
                {head_html}
            </div>
            
            <h2>敘述性統計摘要</h2>
            <div class="table-container">
                {describe_html}
            </div>

            <footer>
                <p>報告生成時間: {generation_time}</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return html_template

def main():
    """
    主執行函式
    """
    # 檢查是否有提供檔案路徑作為參數
    if len(sys.argv) < 2:
        print("錯誤：請提供 CSV 檔案的路徑作為第一個參數。")
        print("用法: python generate_report.py <your_data.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    # 根據輸入檔名決定輸出檔名
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"{base_name}_report.html"

    print(f"正在讀取檔案：{input_file}...")
    try:
        df = pd.read_csv(input_file)
        print("檔案讀取成功，正在生成報告...")
        
        # 生成 HTML 內容
        html_content = generate_html_report(df, input_file)
        
        # 將報告寫入 HTML 檔案
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"報告成功生成！已儲存至：{output_file}")

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"處理過程中發生錯誤：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
