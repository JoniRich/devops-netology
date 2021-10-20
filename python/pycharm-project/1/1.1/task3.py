salary = int(input('Введите заработную плату в месяц: '))
percent_mortgage = int(input('Введите, какой процент(%) уходит на ипотеку:'))
percent_life = int(input('Введите, какой процент(%) уходит на жизнь:'))
year_mortgage = salary * percent_mortgage / 100 * 12
year_life = salary * percent_life / 100 * 12
year_capital = salary * 12 - year_mortgage - year_life
print('На ипотеку было потрачено:', year_mortgage)
print('Было накоплено:', year_capital)