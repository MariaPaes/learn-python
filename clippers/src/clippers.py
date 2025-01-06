hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for cont in prices:
  total_price += cont

average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)

new_prices = [x - 5 for x in prices]
print(new_prices)

total_revenue = 0
i = 0

for i in range():
