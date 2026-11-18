records = [('Order A', 125), ('Order B', 230), ('Order C', 90)]
total = sum(amount for _, amount in records)
for name, amount in records:
    print(f"{name}: {amount}")
print("Total:", total)
print("Average:", round(total / len(records), 2))

