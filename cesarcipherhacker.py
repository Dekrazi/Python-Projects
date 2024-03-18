# Let the user specify the message to hack:
print('Enter a cesar cipher message to hack')
message = input('> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for key in range(len(SYMBOLS)):
    translated = ''

    for i in message:
        if i in SYMBOLS:
            num = SYMBOLS.find(i)
            num = num - key
            
            if num < 0:
                num = num + len(SYMBOLS)

            translated += SYMBOLS[num]
        else:
            translated += i

    print(f'Key #{key}: {translated}')

