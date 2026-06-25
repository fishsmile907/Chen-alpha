import requests
import pandas as pd

# 取得台股全市場資料（公開來源）
url = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"
data = requests.get(url).json()

df = pd.DataFrame(data)

# 轉數字
df["成交金額"] = pd.to_numeric(df["成交金額"].str.replace(",", ""), errors="coerce")

# 篩選流動性（市場有資金進來的）
df = df[df["成交金額"] > 80000000]

# 排序（資金關注度）
top = df.sort_values("成交金額", ascending=False).head(10)

print("=== 今日候選股 ===")
print(top[["證券代號", "證券名稱", "成交金額"]])
