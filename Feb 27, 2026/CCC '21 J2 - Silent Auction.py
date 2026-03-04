n = int(input())

max_bid = -1
winner = ""

for i in range(n):
    name = input()
    bid = int(input())

    if bid > max_bid:
        max_bid = bid
        winner = name

print(winner)