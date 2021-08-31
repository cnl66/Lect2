again = "Ja"
count = 3
# while again == "Ja":
while count > 0:
    print("Skriv in två tal")
    num1 = int(input("Tal1: "))
    num2 = int(input("Tal2: "))

    if num1 > num2:
        print("Tal1 > Tal2")
    elif num2 > num1:
        print("Tal2 > Tal1")
    else:
        print("Tal1 = Tal2")
    count = count - 1    # count -= 1
    # again = input("Vill du upprepa programmet? ")

print("Programmet avslutas ...")
