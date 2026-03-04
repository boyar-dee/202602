n = int(input())

t_count = 0
s_count = 0

for i in range(n):
    line = input()
    t_count += line.count("t") + line.count("T")
    s_count += line.count("s") + line.count("S")

if t_count > s_count:
    print("English")
else:
    print("French")