#Pyydetään käyttäjältä luvut
luku_1 = int(input("Anna ensimmäinen luku:"))
luku_2 = int(input("Anna toinen luku:"))
valinta = True
while valinta:
#Annetaan vaihtoehdot
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Vaihda luvut")
    print("(6) Lopeta")
    #pyydetään valitsemaan
    valinta = input("Tee valinta (1-6):")
    print("Valitut luvut", luku_1, luku_2)
    if valinta == "1":
        print("Tulos on:", luku_1 + luku_2)
    elif valinta == "2":
        print("Tulos on:", luku_1 - luku_2)
    elif valinta == "3":
        print("Tulos on:", luku_1 * luku_2)
    elif valinta == "4":
        print("Tulos on:", luku_1 / luku_2)
    elif valinta == "5":
        luku_1 = int(input("Anna uusi ensimmäinen luku:"))
        luku_2 = int(input("Anna uusi toinen luku:"))
        valinta = True  # Nollataan valinta
    if valinta == "6":
        valinta = False





