# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 420
}

total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter Stock Symbol (AAPL, TSLA, GOOG, MSFT) or 'done' to finish: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid Stock Symbol!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity

    total_value += investment

    print(f"{stock} Investment Value = ${investment}")

print("\n===== PORTFOLIO SUMMARY =====")
print(f"Total Portfolio Value = ${total_value}")

# Save result to file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write(f"Total Portfolio Value = ${total_value}")

print("Summary saved in portfolio_summary.txt")