import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
df_ = pd.read_excel("online_retail_II.xlsx",
                    sheet_name="Year 2010-2011")

#Şirketin gelirlerinin yaklaşık yüzde 80’ini oluşturan ürünleri bulunuz.Bu ürünlerin tüm ürünlere oranı kaçtır?
df = df_.copy()
df.columns
df = df[~df["Invoice"].str.contains("C", na=False)]
df = df[df["Quantity"] > 0]

df.isnull().sum().sum()
df.dropna(inplace=True)

df["Total_Price"] = df["Quantity"] * df["Price"]
df["Total_Price"].sum()


new_df = df.groupby("StockCode").agg({"Total_Price": "sum"}).sort_values("Total_Price", ascending=False)
new_df.reset_index(inplace=True)
total_stock = len(new_df.index)
a = new_df["Total_Price"].sum() * 0.8

price = 0
j = 0
for i in new_df.index:
    if price >= a:
        break
    price = price + new_df.loc[i, "Total_Price"]
    j = j + 1


print(price)
print(j)

print("Oran:", j*100/total_stock)


# Şirketin gelirlerinin yaklaşık yüzde 80'ini oluşturan müşterileri bulunuz. Bu müşterilerin tüm müşterilere oranı kaçtır?



new_df = df.groupby("Customer ID").agg({"Total_Price": "sum"}).sort_values("Total_Price",ascending=False)

new_df.reset_index(inplace=True)
b = 0
customer = 0
for i in range(len(new_df.index)):
    if b >= price:
        break
    b = b + new_df.loc[i,"Total_Price"]
    customer = customer + 1

print(customer)


total_customer = len(new_df.index)

print("ratio",customer*100/total_customer)







