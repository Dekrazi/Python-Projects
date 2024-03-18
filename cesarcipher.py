SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Do you want to (e)ncrypt or (d)ecrypt your message?')
action = input('> ').lower()

while True:
    if action.startswith('e'):
        mode = 'encrypt'
        break
    if action.startswith('d'):
        mode = 'decrypt'
        break
    else:
        print('Invalid choice. Choose from e or d.')
        break

while True:
    max_key = len(SYMBOLS) - 1
    print(f'Please enter the key from 1 to {max_key} to use.')
    response = input('> ')

    if not response.isdecimal():
        continue
    
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print(f'Enter a message to {mode}.')
message = input('> ')
message = message.upper()

translated = ''

for i in message:
    if i in SYMBOLS:
        num = SYMBOLS.find(i)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        num = num % len(SYMBOLS)

        translated += SYMBOLS[num]
    else:
        translated += i

print(f'Your {mode} message:')
print(translated)
