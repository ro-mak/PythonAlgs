from collections import namedtuple

n = int(input("Quantity: "))
l = input("Names and profits: ").split()
names = l[::2]
profits = l[1::2]

Company = namedtuple("Company", "company_name, profit")
company_list = list(map(lambda kv: Company(kv[0], kv[1]), dict(zip(names, map(int, profits))).items()))
total_profit = int(sum(list(map(lambda c: c.profit, company_list))))
average_profit = total_profit // n

print(f"Average profit {average_profit}")
for name, profit in company_list:
    if profit > average_profit:
        print(f"Company {name}'s profit is bigger than average")
    elif profit < average_profit:
        print(f"Company {name}'s profit is lower than average")
