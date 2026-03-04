donuts = int(input())
events = int(input())

for i in range(events):
    sign = input()
    q = int(input())

    if sign == "+":
        donuts = donuts + q
    else:
        donuts = donuts - q

print(donuts)