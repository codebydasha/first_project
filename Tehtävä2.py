'''import math
def tulosta_valikko():
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(luku1/luku2)")
    print("(6) cos(luku1/luku2)")
    print("(7) Vaihda luvut")
    print("(8) Lopeta")


def main():
    luku_1 = int(input("Anna ensimmäinen luku:"))
    luku_2 = int(input("Anna toinen luku:"))
    while True:
        tulosta_valikko()
        print("Valitut luvut:", luku_1, luku_2)
        valinta = input("Tee valinta (1-8):")
        if valinta == "1":
            tulos = luku_1 + luku_2
            print("Tulos on:", tulos)
        elif valinta == "2":
            tulos = luku_1 - luku_2
            print("Tulos on:", tulos)
        elif valinta == "3":
            tulos = luku_1 * luku_2
            print("Tulos on:", tulos)
        elif valinta == "4":
            tulos = luku_1 / luku_2
            print("Tulos on:", tulos)
        elif valinta == "5":
            tulos = math.sin(luku_1 / luku_2)
            print("Tulos on:", tulos)
        elif valinta == "6":
            tulos = math.cos(luku_1 / luku_2)
            print("Tulos on:", tulos)
        elif valinta == "7":
            luku_1 = int(input("Anna uusi ensimmäinen luku:"))
            luku_2 = int(input("Anna toinen luku:"))

        elif valinta == "8":
            print("Lopetetaan")
            break

if __name__ == "__main__":
    main()'''


def luvunpyytaja():
    try:
        luku = int(input("Anna luku:"))
        return luku
    except (TypeError, ValueError):
        print("Virheellinen syöte!")


import math


def tulosta_valikko():
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(luku1/luku2)")
    print("(6) cos(luku1/luku2)")
    print("(7) Vaihda luvut")
    print("(8) Lopeta")


def main():
    flag = True
    flag2 = True
    while flag:
        luku_1 = luvunpyytaja()
        condition = isinstance(luku_1, int)
        if condition:
            flag = False
    while flag2:
        luku_2 = luvunpyytaja()
        condition = isinstance(luku_2, int)
        if condition:
            flag2 = False

    while True:
        valikko = tulosta_valikko()
        print(f"Valitut luvut: {luku_1, luku_2}")
        valinta = input("Tee valinta (1-8):")
        if valinta == "1":
            tulos = luku_1 + luku_2
            print("Tulos on:", tulos)
        elif valinta == "2":
            tulos = luku_1 - luku_2
            print("Tulos on:", tulos)
        elif valinta == "3":
            tulos = luku_1 * luku_2
            print("Tulos on:", tulos)
        elif valinta == "4":
            tulos = luku_1 / luku_2
            print("Tulos on:", tulos)
        elif valinta == "5":
            tulos = math.sin(luku_1 / luku_2)
            print("Tulos on:", tulos)
        elif valinta == "6":
            tulos = math.cos(luku_1 / luku_2)
            print("Tulos on:", tulos)
        elif valinta == "7":
            flag3 = True
            flag4 = True
            while flag3:
                luku_1 = luvunpyytaja()
                condition = isinstance(luku_1, int)
                if condition:
                    flag3 = False
            while flag4:
                luku_2 = luvunpyytaja()
                condition = isinstance(luku_2, int)
                if condition:
                    flag4 = False
        elif valinta == "8":
            break


if __name__ == "__main__":
    main()