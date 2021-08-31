import random  # from random import randint

again = "Ja"
print("Välkommen till singla slant!")

while again == "Ja" or again == "JA" or again == "ja":
    coin = random.randint(0, 1)

    if coin == 0:
        print("Krona")
    else:
        print("Klave")

    print("\nVill du singla slant igen (Ja/Nej)? ")
    again = input()

print("Programmet avslutas ...")
