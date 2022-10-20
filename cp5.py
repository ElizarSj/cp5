number=int(input("ведите_число"))
system=int(input("ведите_номер_системы"))
s=''

while number>0:
    s = str(number % system) + s
    number = number // system

print(s)
