num = int(input())

strings = []
for i in range(0,num):
    string_name = input()
    strings.append(string_name)

for S in strings:
    even = []
    for i in range(0, len(S)):
        if i % 2 == 0:
            even.append(S[i])

    odd = []
    for i in range(0, len(S)):
        if i % 2 != 0:
            odd.append(S[i])

    even = ''.join(even)
    odd = ''.join(odd)
    output = str(even) + ' ' + str(odd)
    print(output)
