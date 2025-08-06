import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# --- 1. 載入與檢視資料 ---
print("載入客戶流失資料集...")
df = pd.read_csv("C:\\Users\\user\\project\\Fundamental-tools-for-data-science\\data\\churn_data.csv")

# 處理 TotalCharges 的缺失值
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)

# 將 'Churn' 轉換為數值
le = LabelEncoder()
df['Churn'] = le.fit_transform(df['Churn'])

# 將 'Gender' 轉換為數值
df['Gender'] = le.fit_transform(df['Gender'])


print("資料集前五行：")
print(df.head())
print("\n資料集基本資訊：")
df.info()

# --- 2. 特徵重要性分析 ---
print("\n正在計算特徵重要性...")
X = df.drop(['Churn','CustomerID'], axis=1)
y = df['Churn']

# 訓練隨機森林模型
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 獲取特徵重要性
importances = pd.Series(model.feature_importances_, index=X.columns)
top_3_features = importances.nlargest(3)

print("\n影響客戶流失最重要的三個變數：")
print(top_3_features)

# --- 3. 資料視覺化 ---
most_important_feature = top_3_features.index[0]
print(f"\n正在視覺化 '{most_important_feature}' 與流失率的關係...")

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x=most_important_feature, hue='Churn', multiple='fill', stat='proportion', shrink=.8)
plt.title(f'Churn Rate by {most_important_feature}')
plt.ylabel('Proportion of Customers')
plt.xlabel(most_important_feature)
plt.legend(title='Churn', labels=['Yes', 'No'])

# 儲存圖表
plt.savefig("churn_by_tenure.png")
print("圖表已儲存為 churn_by_tenure.png")