import pandas as pd

# 建立一個範例 DataFrame
data = {'category': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
        'sales': [100, 200, 50, 300, 150, 400, 250, 500]}
df = pd.DataFrame(data)

# 這是一行複雜的 Pandas 操作，目的是找出每個分類中銷售額前兩名的紀錄
# The one-liner to be explained by Gemini
result = df.groupby('category').apply(lambda x: x.nlargest(2, 'sales')).reset_index(drop=True)

print("每個分類中銷售額前兩名的紀錄：")
print(result)
