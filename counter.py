
counter = 0

while True:
    print(f'Current count: {counter}')
    print('Menu:',
          '(I)ncrement',
          '(D)ecrement',
          '(R)eset',
          '(E)xit')
    user_choice = input('What\'s next? ')
    if user_choice == 'I'.lower():
       counter += 1
    elif user_choice == 'D'.lower():
        counter -= 1
    elif user_choice == 'R'.lower():
        counter = 0
    elif user_choice == 'E'.lower():
        break
    else:
        print('Invalid choice. Choose from I, D, R or E')
        
        

    
