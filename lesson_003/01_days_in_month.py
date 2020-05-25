
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
# TODO Используйте оператор in. С ним вы можете гарантировано убедиться,
#  что элемент является ключом словаря.
#  if month in days_in_month
if month > 12:
    print("Не корректный номер месяца ->", month)
else:
    print("в месяце с номером ", month, days_in_month.get(month), "дней")
