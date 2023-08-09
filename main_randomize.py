# Žaidimas kryžiukai/nuliukai by MarMa
import random


class Zaidejas:
    def __init__(self, vardas, simbolis, pergales):
        self.vardas = vardas
        self.simbolis = simbolis
        self.pergales = pergales

    def __str__(self):
        return f"Vardas: {self.vardas}, simbolis: '{self.simbolis}', pergalių sk. {self.pergales}"

def lenteles_formavimas():
    global lentele
    lentele = []
    for i in range(3):
        for j in range(3):
            lentele.append(" ")
    lenteles_spausdinimas()


def lenteles_spausdinimas():  # spausdinama 3x3 lentelė su tarpais
    print("    1    2    3")
    for i in range(3):
        print(i + 1, lentele[i * 3:i * 3 + 3])


def nr_ivedimas(zaidejas, simb):  # kiekvienas žaidėjas įveda dviženklį skaičių, kuris paverčiamas eil/stul nr.
    flag = True
    while flag == True:
        try:
            nr = str(input(f'"{simb}" {zaidejas} įveskite dviženklį skaičių '))
            if int(nr) > 10 and int(nr) < 14 or int(nr) > 20 and int(nr) < 24 or int(nr) > 30 and int(nr) < 34:
                i = int(nr[0]) - 1
                j = int(nr[1]) - 1
                if lentele[i * 3 + j] == " ":  # įvesti galima tik į tuščią langelį
                    lentele[i * 3 + j] = simb
                    flag = False
                else:
                    print("Užimtas langelis, kartokite")
            else:
                print("neteisingai įvestas skaičius")
        except ValueError:
            print("neteisingai įvestas simbolis")
    lenteles_spausdinimas()


def kompiuterio_ivedimas(zaidejas, simb):  # kompiuteris įveda atsitiktinį skaičių 0...8
    flag = True
    while flag == True:
        num = int(random.randint(0, 8))
        print(num)
        if lentele[num] == " ":  # įvesti galima tik į tuščią langelį
            lentele[num] = simb
            flag = False
    lenteles_spausdinimas()


# tikrinama ar laimėjo kuris nors žaidėjas (horizontaliai, vertikaliai, įstrižai)
def ar_laimejo(lentele, pozymis):
    laimejo = False
    for x in range(3):
        if lentele[x * 3] == pozymis and lentele[x * 3 + 1] == pozymis and lentele[x * 3 + 2] == pozymis: laimejo = True
        if lentele[x] == pozymis and lentele[x + 3] == pozymis and lentele[x + 6] == pozymis: laimejo = True
    if lentele[0] == pozymis and lentele[4] == pozymis and lentele[8] == pozymis: laimejo = True
    if lentele[2] == pozymis and lentele[4] == pozymis and lentele[6] == pozymis: laimejo = True
    return laimejo


def ar_lygiosios(lentele):  # jei pasibaigė langeliai ir niekas nelaimėjo - tai lygiosios
    if " " in lentele:
        return False
    else:
        return True


# pradinis žaidėjų vardų įvedimas
nuliuku_zaidejas = input("Nuliukais žais? ")
zaidejas0 = Zaidejas(nuliuku_zaidejas, "0", 0)
kryziuku_zaidejas = "Kompiuteris"
zaidejasX = Zaidejas(kryziuku_zaidejas, "X", 0)
print("Žaidimo pradžia ", zaidejas0)
print("Žaidimo pradžia ", zaidejasX)
print("---------------------------\n Įveskite dviženklį skaičių\n eilutės nr. ir stulpelio nr. \n pvz. '11' '33'")

# formuojame Žaidimo lentelę
lenteles_formavimas()

zaid = "t"  # bus žaidžiama tol, kol zaid reiksmė pasikeis
while zaid == "t":
    nr_ivedimas(zaidejas0.vardas, zaidejas0.simbolis)
    if (ar_laimejo(lentele, zaidejas0.simbolis)):
        print(f"laimėjo  {zaidejas0.vardas}")
        zaidejas0.pergales += 1
        print("rezultatas", zaidejas0.vardas, zaidejas0.pergales, zaidejasX.vardas, zaidejasX.pergales)
        zaid = input("Ar dar žaisite? t/n ")
        if zaid == "t":
            lentele = "         "
            lenteles_formavimas()
        else:
            exit()
    elif ar_lygiosios(lentele) == True:
        print("lygiosios ")
        print("rezultatas", zaidejas0.vardas, zaidejas0.pergales, zaidejasX.vardas, zaidejasX.pergales)
        zaid = input("Ar dar žaisite? t/n ")
        if zaid == "t":
            lenteles_formavimas()
        else:
            exit()

    kompiuterio_ivedimas(zaidejasX.vardas, zaidejasX.simbolis)
    if (ar_laimejo(lentele, zaidejasX.simbolis)):
        print(f"laimėjo  {zaidejasX.vardas}")
        zaidejasX.pergales += 1
        print("rezultatas", zaidejas0.vardas, zaidejas0.pergales, zaidejasX.vardas, zaidejasX.pergales)
        zaid = input(str("Ar dar žaisite? t/n "))
        if zaid == "t":
            lenteles_formavimas()
        else:
            exit()
    elif ar_lygiosios(lentele) == True:
        print("lygiosios ")
        print("rezultatas", zaidejas0.vardas, zaidejas0.pergales, zaidejasX.vardas, zaidejasX.pergales)
        zaid = input("Ar dar žaisite? t/n ")
        if zaid == "t":
            lenteles_formavimas()
