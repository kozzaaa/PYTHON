#############################################################
#
# Lekcja: 20.02
#
#############################################################

dane = "Jan Kowlaski"
print(dane[0])
print(dane[0:3])
print(dane[4:])
print(dane[:3])
print(dane[4:-1])

kodPocztowy = "22*375"
znak = "-"
print(kodPocztowy[:2] + znak + kodPocztowy[3:])

name = "Adam"
print(id(name))
name = "Iga"
print(id(name))

# Każda zmienna jest traktowana jako obiekt.

dane = "Jan Kowalski"
print(type(dane))

# Split dzieli nam na komórki po spacji.

print(dane.split())

# Podział na elemnty

print(dane.split(sep = "-"))

dane = "Jan-Kowalski.20"
dane = "'" + dane[:3] + "', '" + dane[4:12] + "', '" + dane[-2:16] + "'"
print(dane)



#############################################################
#
# Lekcja: 24.02
#
#############################################################

# Zmienna: len liczy każdy znak oraz spacje.

# Zmienna: range podaje sekwencję liczb na podstawie podanego indeksu początku i końca.

# Zmienna: def może być skrótem od "define", czyli "zdefiniuj", albo "definition", czyli "definicja"

s1 = "biologia"
s2 = "molekularna"

print(s1 + " " + s2)
print(s1, s2)

n1 = s1 + " " + s2
print(len(n1))

for name in n1:
    print(name)
    
for name1 in range(len(n1)):
    print(n1[name1])

def ile(s):
    ile_A = 0
    ile_C = 0
    ile_G = 0
    ile_T = 0
    for z in s:
        if z == "A":
            ile_A += 1
        elif z == "C":
            ile_C += 1
        elif z == "G":
            ile_G += 1
        else:
            ile_T += 1
    return[ile_A, ile_C, ile_G, ile_T]
print("CAATAAAAAAG")
print("[A, C, G, T]")
print(ile("CAATAAAAAAG"))

#############################################################
#
# Lekcja: 27.02
#
#############################################################
dane = "Jan Kowalski"
print(dane.count("a"))

# replace: Zamienia znak.

kodPodczowy = "22)300"
print(kodPodczowy.replace(")", "-"))
print(kodPodczowy.replace(kodPodczowy[2], "-"))

dane = "Jan Kowalski"

# find: Pokazuje na jakiej pozycji jest dany znak lub ciąg liter.

# index: Działa tak samo jak "find" ale gdy nie ma znaku lub ciągu lter program nie będzie działać

print(dane.find("s"))
print(dane.index("s"))

print(dane)
print(len(dane))

# rstrip: Usuwa spacje z prawje storny.

# lstrip: Usuwa spacje z lewej strony.

dane = dane.rstrip()

name = "Miłosz"

# endswith: Sprawdza końcowy znak lub literę.

print(name.endswith("a"))

# wiek.isdigit(): Sprawdza czy przypomina liczbę.

wiek = "20"
print(wiek.isdigit())

# isupper(): Sprawdza czy pierwsza litrera zdania wyrazu jest z dużej litery.

zdanie = "O 16:30 kończymy zajecia"
print(zdanie[0].isupper())

