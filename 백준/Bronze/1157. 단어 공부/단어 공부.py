x = input()

x = x.upper()
x_li = list(set(x))
count = []

for i in x_li:
    a = x.count(i)
    count.append(a)

if count.count(max(count)) >=2:
    print("?")
else:
    print(x_li[(count.index(max(count)))])