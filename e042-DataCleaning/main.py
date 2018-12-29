import pandas as pd

path = "amazon_items.csv"
data = pd.read_csv(path)
print(data.head())


list_of_prices = []
for i in data["price"]:
    list_of_prices.append(float(str(i).replace("EUR", "").replace(",", ".").strip()))

data["price"] = list_of_prices


list_of_titles = []
for i in data["title"]:
    if str(i).lower().count("samsung galaxy s8 plus") > 0:
        list_of_titles.append("Samgung Galaxy S8 Plus")
    else:
        list_of_titles.append("Samgung Galaxy S8")

data["title"] = list_of_titles


list_of_stars = []
for i in data["stars"]:
    list_of_stars.append(str(i).partition("de un")[0])

data["stars"] = list_of_stars


list_of_customer_reviews = []
for i in data["customer_reviews"]:
    list_of_customer_reviews.append(str(i).partition("opiniones")[0])

data["customer_reviews"] = list_of_customer_reviews


list_of_recommended_price = []
for i in data["recommended_price"]:
    if str(i) != "nan":
        list_of_recommended_price.append(str(i).upper().replace("EUR", "").strip())
    else:
        list_of_recommended_price.append(0)

data["recommended_price"] = list_of_recommended_price


list_of_ram = []
for i in data["RAM"]:
    if str(i).count("GB") > 0:
        RAM = str(i).replace("GB", "").strip()
        if int(RAM) < 15:
            list_of_ram.append(RAM)
        else:
            list_of_ram.append(0)
    else:
        list_of_ram.append(0)

data["RAM"] = list_of_ram


list_of_rom = []
for i in data["ROM"]:
    if str(i).count("GB") > 0:
        ROM = str(i).replace("GB", "").strip()
        if int(ROM) > 15:
            list_of_rom.append(ROM)
        else:
            list_of_rom.append(0)
    else:
        list_of_rom.append(0)

data["ROM"] = list_of_rom


# We delete the data that does not interest us (for example, phone cases) and we only leave the mobile data
df = data.drop(data[data.price < data["price"].mean()].index)

# We order the values (descending titles and ascending prices)
df = df.sort_values(['title', 'price'], ascending=[0, 1])


print(df.head())
df.to_csv("new_amazon_items.csv")


"""
import webbrowser

for i in df["url"]:
    webbrowser.open(i)
"""
