# my_analysis.R

# 建立一個 R 的 data.frame
df <- data.frame(
  Name = c("Apple", "Banana", "Apple", "Orange", "Banana"),
  Count = c(10, 20, 15, 5, 25)
)

# 使用 R base 語法計算每種水果的總數
agg_df <- aggregate(df$Count, by=list(Category=df$Name), FUN=sum)

# 列印結果
print(agg_df)
