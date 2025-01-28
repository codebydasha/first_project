''''try:
    tiedosto = input("Anna tiedoston nimi:")
    my_file = open(tiedosto, "r")
    content = my_file.read()
    my_file.close()
    tulos = int(content) + 313
except IOError:
    print("Virheellinen tiedostonnimi")
except ValueError:
    print("Tiedoston sisältö virheellinen!")
else:
    print("Tulos on", tulos)'''

'''koordinaatit = (123, 133)
print(koordinaatit)
print(koordinaatit[1])
koordinaatit[1] = 1001'''

'''lista =[]
while True:
    try:
        print("Haluatko")
        print("(1)Lisätä listaan")
        print("(2)Poistaa listalta vai")
        valinta = input("(3)Lopettaa?:")
        if valinta == "1":
            lisa = input("Mitä lisätään?:")
            lista.append(lisa)
        elif valinta == "2":
            try:
                maara = len(lista)
                print("Listalla on", maara, "alkiota.")
                valinta = int(input("Monesko niistä poistetaan?:"))
                lista.pop(valinta)
            except ValueError:
                print("Virheellinen valinta")
        elif valinta == "3":
            print("Listalla oli tuotteet:")
            for i in lista:
                print(i)
            break
    except (IndexError,ValueError):
        print("Virheellinen valinta.")ä'''

tidosto = open("tiedosto.txt", r)
sisalto = tiedosto.readlines()
print(sisalto)
for i in sisalto:
    print(i)
tiedosto.close()




