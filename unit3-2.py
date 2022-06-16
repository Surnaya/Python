name = input("Введите имя: ")
surname = input("Введите фамилия: ")
year = input("Дата рождения: ")
city = input("Введите город: ")
email = input("Введите ваш emal: ")
tel = input("Ваш телефон: ")

def info(name, surname, year, city, email, tel):
    print(f"name - {name}, surname - {surname}, yaer - {year}, city - {city}, email - {email}, tel - {tel}")

info(name, surname, year, city, email, tel)

