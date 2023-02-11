import calendar

username = input('Please enter your name: ')
print(f'Hello {username}\n')

year = int(input('Please enter an year: '))
month = int(input('Please enter a month: '))

print(calendar.month(year, month))

print('Good bye')