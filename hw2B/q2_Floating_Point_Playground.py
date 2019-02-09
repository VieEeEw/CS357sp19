a = 2**53 + 1
k = 0
i = 0
while True:
    print(i, "===")
    if a == a + 10 ** -i:

        # print(a + 10 ** -i,end=",")
        k = -i + 1
        break
    i+= 1
    # a += 10 ** -i
print(k)

i = 0
while True:
    # print(i, "===")
    if a == a + 10 ** -i:

        # print(a + 10 ** -i, end=",")
        k = -i + 1
        break
    a += 10 ** -i
    i += 1

print(k)