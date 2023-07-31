"""pradinių duomenų nustatymas:
Žaidėjas vienas "nuliuku_zaidejas 0"
Žaidėjas antras "kryziuku_zaidejas "
"""

def lenteles_spausdinimas(lentele):     # spausdinama 3x3 lentelė
    print("    1    2    3")
    for i in range(3):
        print(i + 1, lentele[i*3:i*3+3])
def nr_ivedimas(zaidejas,simb):
    flag=True
    while flag==True:
        nr = str(input(zaidejas))
        if int(nr)>10 and int(nr) <34:
            i = int(nr[0]) - 1
            j = int(nr[1]) - 1
            if lentele[i * 3 + j] == " ":
                lentele[i * 3 + j] = simb
                flag=False
            else:
                print("Užimtas langelis, kartokite")
        else:
            print("neteisingai įvestas skaičius")
    lenteles_spausdinimas(lentele)


# tikrinama ar laimėjo
def ar_laimejo(lentele,pozymis):
    # horizontaliai
    laimejo=False
    for x in range(3):
        if lentele[x*3]==pozymis and lentele[x*3+1]==pozymis and lentele[x*3+2]==pozymis : laimejo=True
        if lentele[x]==pozymis and lentele[x+3]==pozymis and lentele [x+6] == pozymis : laimejo=True
    if lentele[0]==pozymis and lentele[4]==pozymis and lentele [8] == pozymis : laimejo=True
    if lentele[2]==pozymis and lentele[4]==pozymis and lentele [6] == pozymis : laimejo=True
    return laimejo
def ar_lygiosios(lentele):
    if  " " in lentele: return False
    else: return True

# nuliuku_zaidejas=input("Nuliukais žais? ")
# kryziuku_zaidejas=input("Kryziukais žais? ")
nuliuku_zaidejas="Marius "
kryziuku_zaidejas="Tadas "
print("0  ",nuliuku_zaidejas, "X  ",  kryziuku_zaidejas)
"""formuojame Žaidimo matricą"""
lentele = []
for i in range(3):
    for j in range(3):
        lentele.append(" ")
lenteles_spausdinimas(lentele)
kryziuku_pergales=0
nuliuku_pergales=0
zaid="t"
while zaid=="t":
    nr_ivedimas(nuliuku_zaidejas,"0")
    if(ar_laimejo(lentele,"0")):
        print(f"laimėjo  {nuliuku_zaidejas}")
        nuliuku_pergales +=1
        print("rezultatas",nuliuku_zaidejas, nuliuku_pergales, kryziuku_zaidejas, kryziuku_pergales)
        zaid = input("Ar dar žaisite? t/n ")
        if zaid=="t":
            lentele = []
            for i in range(3):
                for j in range(3):
                    lentele.append(" ")
            lenteles_spausdinimas(lentele)
        else: exit()
    elif ar_lygiosios(lentele)==True:
        print("lygiosios ")
        print("rezultatas",nuliuku_zaidejas, nuliuku_pergales, kryziuku_zaidejas, kryziuku_pergales)
        zaid = input("Ar dar žaisite? t/n ")
        if zaid == "t":
            lentele = []
            for i in range(3):
                for j in range(3):
                    lentele.append(" ")
            lenteles_spausdinimas(lentele)
        else: exit()

    nr_ivedimas(kryziuku_zaidejas,"X")
    if (ar_laimejo(lentele, "X")):
        print(f"laimėjo  {kryziuku_zaidejas}")
        kryziuku_pergales =+1
        print("rezultatas",nuliuku_zaidejas, nuliuku_pergales, kryziuku_zaidejas, kryziuku_pergales)
        zaid = input(str("Ar dar žaisite? t/n "))
        if zaid=="t":
            lentele = []
            for i in range(3):
                for j in range(3):
                    lentele.append(" ")
            lenteles_spausdinimas(lentele)
        else: exit()
    elif ar_lygiosios(lentele)==True:
        print("lygiosios ")
        print("rezultatas",nuliuku_zaidejas, nuliuku_pergales, kryziuku_zaidejas, kryziuku_pergales)
        zaid = input("Ar dar žaisite? t/n ")
        if zaid == "t":
            lentele = []
            for i in range(3):
                for j in range(3):
                    lentele.append(" ")
            lenteles_spausdinimas(lentele)"# naujas" 
