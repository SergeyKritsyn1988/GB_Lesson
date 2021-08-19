km = int(input("Enter the distance :"))
final_km = int(input("Enter final killometrs :"))
days = 1
while km < final_km:
    km *= 1.1
    days += 1
print(days)
