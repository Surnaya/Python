time = input("Введите время в секундах:")
hours = int(time) // 3600
a = int(time) % 3600
minutes = a // 60
seconds = a % 60

print(f"Время: {hours}:{minutes}:{seconds}")
