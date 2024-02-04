

output = 0

for i in range(111112):
    x = str(i)
    result = [int(i) for i in x]

    if sum(result) == 6 and 0 not in result:
        print(x)
        output += 1


print(output)