mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
[n for n in mylist if n < 0]
prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}

p1 = {key:value for key, value in prices.items() if value > 200}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p1)
print(p2)