a1 = int(input())
a2 = int(input())
a3 = int(input())

b1 = int(input())
b2 = int(input())
b3 = int(input())

apples = 3*a1 + 2*a2 + a3
bananas = 3*b1 + 2*b2 + b3

if apples > bananas:
    print("A")
elif bananas > apples:
    print("B")
else:
    print("T")