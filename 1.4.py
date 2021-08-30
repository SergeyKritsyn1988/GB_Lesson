umber = int(input("please enter a number "))
m = number % 10
number = number // 10
while number > 0:
    if number % 10 > m:
        m = number % 10
    number = number // 10
print(m)
