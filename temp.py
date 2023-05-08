

profit = []
prices = [7,1,5,3,6,4]

for price in prices:
    for i in range(len(prices)):
        buy_price = price
        # print(buy_price)
        try:
            sell_price = max(prices[i+1:])
        except ValueError:
            pass
        # print(sell_price)
        profit.append(sell_price - buy_price)
if max(profit))


# print(range(len(prices)))