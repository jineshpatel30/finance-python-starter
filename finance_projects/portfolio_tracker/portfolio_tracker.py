# Portfolio Tracker with lists

assets = ["Stock A", "Stock B", "Bond C"]
values = [3000, 2000, 5000]   # current values in USD

total = 0
for v in values:
    total += v

print("Holdings:")
for i in range(len(assets)):
    print(f"{assets[i]}: {values[i]}")

print("Total Portfolio Value:", total)

# To Do: store in dictionary instead of lists, calculate weights and handle live price.