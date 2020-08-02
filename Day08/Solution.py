n =  int(input())

entries = [input().split() for i in range(n)]
phoneBook = {key:val for key,val in entries}

while True:
    try:
        name = input()
        if name in phoneBook:
            print('%s=%s' % (name, phoneBook[name]))
        else:
            print('Not found')
    except EOFError:
         break
