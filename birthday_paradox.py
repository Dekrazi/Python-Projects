import datetime, random

def get_birthdays(number_of_birthdays):
    birthdays = []
    
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2024, 1, 1)

        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA

print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
  
  The birthday paradox shows us that in a group of N people, the odds
  that two of them have matching birthdays is surprisingly large.
  This program does a Monte Carlo simulation (that is, repeated random
  simulations) to explore this concept.
  
  (It's not actually a paradox, it's just a surprising result.)
  ''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
print()

print('Here are', num_bdays, 'girthdays:')
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        date_text = '{} {}'.format(month_name, birthday.day)
        print(date_text, end='')
print()
print()

match = get_match(birthdays)

print('In this simulation, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = '{} {}'.format(month_name, match.day)
    print('multiple people have a birthday on', date_text)
else:
    print('there are no matching birthdays.')
print()

print('Generating', num_bdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
sim_match = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match += 1
print('100,000 simulations run.')

probability = round(sim_match / 100000 * 100, 2)
print('Out of 100,000 simulations of', num_bdays, 'people, there was a')
print('matchng birthdays in that group', sim_match, 'times. This maeans')
print('that', num_bdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
