from sys import argv

stake, hours, bonus = argv

def salary (stake, hours, bonus):
    return float(hours) * float(stake) + float(bonus)

print(salary(argv[1], argv[2], argv[3]))