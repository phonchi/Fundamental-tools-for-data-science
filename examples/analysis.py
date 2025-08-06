import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# --- 1. 載入與檢視資料 ---
print("載入 Scikit-learn 中的鳶尾花 (Iris) 資料集...")
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

print("資料集前五行：")
print(df.head())
print("\n資料集基本資訊：")
df.info()

# --- 2. 資料視覺化 ---
print("\n正在生成特徵關係圖 (Pair Plot)...")
sns.pairplot(df, hue='species')
plt.suptitle("Iris Dataset Pair Plot", y=1.02)
# 在非互動式環境中，你可能需要儲存圖片而非顯示
# plt.savefig("iris_pair_plot.png")
print("視覺化步驟完成。")


# --- 3. 簡單模型訓練 ---
print("\n準備訓練一個簡單的分類模型...")
# 將特徵和目標變數分開
X = df.drop('species', axis=1)
y = df['species']

# 切分訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print(f"訓練集大小: {X_train.shape[0]}, 測試集大小: {X_test.shape[0]}")

# 訓練邏輯斯迴歸模型
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print("模型訓練完成。")

# --- 4. 模型評估 ---
print("\n評估模型表現...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"模型在測試集上的準確率 (Accuracy): {accuracy:.2f}")
