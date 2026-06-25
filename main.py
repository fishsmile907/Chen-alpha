import requests
import pandas as pd

url = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"
data = requests.get(url).json()

df = pd.DataFrame(data)

df["成交金額"] = pd.to_numeric(df["成交金額"].str.replace(",", ""), errors="coerce")

df = df[df["成交金額"] > 80000000]

top = df.sort_values("成交金額", ascending=False).head(3)

print("=== RUN 結果 ===")

for i, row in top.iterrows():
    print(row["證券名稱"], row["證券代號"], row["成交金額"])
