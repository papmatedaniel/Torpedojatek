import time
import os
import copy

tabla = [["A)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["B)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["C)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["D)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["E)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["F)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["G)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["H)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["I)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["J)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["  ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

tabla1 = []
tabla2 = []
hajoklista = [{
    "ennyiVan": 0,
    "hajoHossz": 4,
    "maxDb": 1,
    'megsemmisulte': 0,
    'eltaltkoordinatak': [],
    "koordinatak": [],
    "mellettekord.": []
}, {
    "ennyiVan": 0,
    "hajoHossz": 6,
    "maxDb": 1,
    'megsemmisulte': 0,
    'eltaltkoordinatak': [],
    "koordinatak": [],
    "mellettekord.": []
}, {
    "ennyiVan": 0,
    "hajoHossz": 1,
    "maxDb": 1,
    'megsemmisulte': 0,
    'eltaltkoordinatak': [],
    "koordinatak": [],
    "mellettekord.": []
}, {
    "ennyiVan": 0,
    "hajoHossz": 2,
    "maxDb": 1,
    'megsemmisulte': 0,
    'eltaltkoordinatak': [],
    "koordinatak": [],
    "mellettekord.": []
}, {
    "ennyiVan": 0,
    "hajoHossz": 3,
    "maxDb": 1,
    'megsemmisulte': 0,
    'eltaltkoordinatak': [],
    "koordinatak": [],
    "mellettekord.": []
}, {
    "ennyiVan": 0,
    "hajoHossz": 5,
    "maxDb": 1,
    'megsemmisulte': 0,
    'eltaltkoordinatak': [],
    "koordinatak": [],
    "mellettekord.": [],
}]
hajoklista1 = []  #lista melybe tároljuk a játékos hajóinak tulajdonságait
hajoklista2 = []  # lista melybe tároljuk a játékos hajóinak tulajdonságait
hajokordinatak = []  #előző hajók koordinátái
hajokordinatak1 = []  # külön eltároljuk a játékosok hajóinak koordinátáit
hajokordinatak2 = []  # külön eltároljuk a játékosok hajóinak koordinátáit
hajokmelletikord = []  #előzőhajók melletti koordináták


def tablamegjelenito() -> None:
    """
    Megjelenítit a táblát
    """
    [print(*i) for i in tabla]


def szamlalod() -> tuple:
    """A számlálóba eltárolja hogy hány hajó koordinátái lettek letéve
    és az alapján indexeli a hajokat tartalmazo lista aktualis hajo szotarat
    A szamlalo2 pedig az éppen aktuális hajó hosszát gyűjti ki, amit majd átadunk
    a valid_e_a_hajo függvények
    """
    szamlalo = sum(1 for i in hajoklista if i["ennyiVan"] == 1)
    szamlalo2 = hajoklista[szamlalo]["hajoHossz"]
    return szamlalo, szamlalo2


def koordinataellenorzo(koordinata: str):
    """
    Ellenőrzi hogy a koordináta az egy irányból és egy koordinátából áll, vagy
    csak egy koordinátából, koordináta A-J-ig, 0-9-ig, irányok pedig, le, fel,
    bal, jobb, ha valamelyik paraméternek nem felel meg, akkor új koordinátá kell
    megadni
    """
    if len(koordinata) > 7 or len(koordinata) < 2:
        return "Túl rövid, min 2 karakteres a koordináta" \
        if len(koordinata) < 2 else \
        '''Túl hosszú, pl A0 jobb-nál nem lehet hosszabb'''

    elem = koordinata.split()
    if len(elem) > 2:
        return "HIBA"

    betu, szam = elem[0][0].upper(), elem[0][1:]
    if betu not in "ABCDEFGHIJ" or szam not in "0123456789":
        return "\nA-J-ig add meg a koordináta első részét\n" \
        if betu not in "ABCDEFGHIJ" else \
        "\n0-9-ig add meg a koordináta második részét\n"

    if len(elem) == 2:
        irany = elem[1].upper()
        if irany not in ["LE", "FEL", "BAL", "JOBB"]:
            return "\nHIBA\n"

    return (elem[0], elem[1]) if len(elem) == 2 else elem


def valid_e_a_hajo(a0: str, betu, szam: int) -> (str | list[str]):
    """
    # -> list or str
    Ez a függvény számolja ki a megadott koordinátából és irányból
    le,fel,bal, jobb, a hajó összes koordinátáját, amit majd a tablamodositonak
    atadunk. Emellett vizsgálja hogy a megadott irány és koordináta táblán
    belül van, és nem kerül e egymás mellé kettő hajó, és eszerint tér vissza
    hiba üzenettel
    """

    kordinatak = [a0.upper()] if len(a0) == 2 else []
    if len(a0) > 3:
        iranyok = {
            "FEL": (-1, 0),
            "LE": (1, 0),
            "JOBB": (0, 1),
            "BAL": (0, -1)
        }
        pont = iranyok[a0.upper()[3:]]
        kordinatak.append(a0[0:2].upper())

        while True:
            betu, szam = "ABCDEFGHIJ".index(a0[0].upper()), int(a0[1])
            if 0 <= betu + pont[0] < 10 and 0 <= szam + pont[1] < 10:
                a0 = chr(ord("A") + betu + pont[0]) + str(szam + pont[1])
                kordinatak.append(a0)
            else:
                break
            if len(kordinatak) == szamlalo2: break

    khmk = set(kordinatak) & set(hajokmelletikord)
    khk = set(kordinatak) & set(hajokordinatak)

    if khmk or khk:
        if khmk and khk:
            return " ".join(("\nEgymás mellé tennél 2 hajót ponton", *khmk,
                             "\nÉs ide már tettél hajót:", *khk, "\n"))
        elif khmk:
            return f"\nEgymás mellé tennél 2 hajót ponton/tokon: {khmk}\n"
        else:
            return f"\nÉs ide már tettél hajót: {khk}\n"
    elif szamlalo2 == len(kordinatak):
        return kordinatak
    else:
        return "\nKilógna a tábláról a hajód, vagy nem adtál meg irányt, adj meg új irányt/koordinátát\n"


def koordinataszamolo(betu, szam: int) -> list:
    """
    Chatgt ihletett, a függvény célja a megadott koordináta melletiti lévő koordináták
    kigyűjtése, hogy aztán ne lehessen 2 hajót egymás mellé tenni
    """
    koordinatak = []

    pontok = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1),
              (1, 1)]

    for pont in pontok:
        if 0 <= betu + pont[0] < 10 and 0 <= szam + pont[1] < 10:
            koordinatak.append(
                chr(ord("A") + betu + pont[0]) + str(szam + pont[1]))

    return [i for i in koordinatak if len(i) == 2]


def tablamodosito(koordinata: str) -> None:
    """A véglegesített hajó koordinátáit elhelyezi a táblán"""
    ytengely = int("ABCDEFGHIJ".index(koordinata[0]))
    xtengely = int(koordinata[1])
    for s, z in enumerate(tabla):
        if s == ytengely:
            z[xtengely + 1] = "X"
            if koordinata not in hajokordinatak:
                hajokordinatak.append(koordinata)


elso = input("Add meg a neved első játékos: ")
masodik = input("\nAdd meg a neved második játékos: ")

while True:
    """A jétkosok hajóinak lerakását, hajók eltárolását \
    szolgálja a while ciklus"""
    os.system("clear")  # töröld a console tartalmát
    if len(hajokordinatak) == 21 and len(hajokordinatak1) == 0:
        hajokordinatak1.extend(hajokordinatak)
        hajokordinatak = []
        hajokmelletikord = []
        kordinatak = []
        hajoklista1 = [dict(i) for i in hajoklista]
        for i in hajoklista:
            for k, v in i.items():
                if k == "ennyiVan":
                    i["ennyiVan"] = 0
                if k == "koordinatak":
                    i["koordinatak"] = []
                if k == "mellettekord.":
                    i["mellettekord."] = []

        tabla1.extend(tabla)
        tabla = [['.' if k == 'X' else k for k in i] for i in tabla]

    if len(hajokordinatak) == 21 and len(hajokordinatak1) == 21:
        hajokordinatak2.extend(hajokordinatak)
        hajokordinatak = []
        hajokmelletikord = []
        kordinatak = []
        hajoklista2 = [dict(i) for i in hajoklista]
        for i in hajoklista:
            for k, v in i.items():
                if k == "ennyiVan":
                    i["ennyiVan"] = 0
                if k == "koordinatak":
                    i["koordinatak"] = []
                if k == "mellettekord.":
                    i["mellettekord."] = []

        tabla2.extend(tabla)
        tabla = [['.' if k == 'X' else k for k in i] for i in tabla]
        break
    tablamegjelenito()

    szamlalod()
    szamlalo2 = szamlalod()[1]
    szamlalo = szamlalod()[0]

    koordinata = input(
        f"\n{elso} Add meg az {szamlalo+1}. hajód első koordinátáját, teljes hajóhossz {szamlalo2} \n\n Ha hajóhossz nagyobb mint 1, akkor egy irányt is adj meg, pl e5 le vagy e5 fel vagy e5 bal vagy e5 jobb " if len(hajokordinatak1) == 0 \
        else \
        f"\n{masodik} Add meg az {szamlalo+1}. hajód első koordinátáját, teljes hajóhossz {szamlalo2} \n\n Ha hajóhossz nagyobb mint 1, akkor egy irányt is adj meg, pl e5 le vagy e5 fel vagy e5 bal vagy e5 jobb "
    ).upper()

    ellenorzo = koordinataellenorzo(koordinata)
    if isinstance(ellenorzo, (list, tuple)):
        betu = "ABCDEFGHIJ".index(koordinata[0].upper())
        szam = int(koordinata[1])
        ellenorzo = valid_e_a_hajo(koordinata, betu, szam)
        if isinstance(ellenorzo, list):
            hajo = hajoklista[szamlalo]
            for elem in valid_e_a_hajo(koordinata, betu, szam):
                betu = "ABCDEFGHIJ".index(elem[0].upper())
                szam = int(elem[1])
                hajo["koordinatak"].append(elem)
                hajo["mellettekord."].extend(koordinataszamolo(betu, szam))
                hajo["mellettekord."] = list(
                    set(hajo["mellettekord."]) - set(hajo["koordinatak"]))
                tablamodosito(elem)
                os.system("clear")
                if hajo["hajoHossz"] == len(hajo["koordinatak"]):
                    hajo["ennyiVan"] += 1

            tablamegjelenito()

            hajokmelletikord.extend([
                m for m in hajo["mellettekord."] if m not in hajokmelletikord
            ])

            if len(input("\nKilépéshez nyomj entert: ")) <= 0: continue

        else:
            os.system("clear")
            tablamegjelenito()
            print(valid_e_a_hajo(koordinata, betu, szam))
            if len(input("\nKilépéshez nyomj entert: ")) <= 0: continue

    else:
        os.system("clear")
        tablamegjelenito()
        print(koordinataellenorzo(koordinata))
        if len(input("\nKilépéshez nyomj entert: ")) <= 0: continue

os.system("clear")
hajoklista1 = copy.deepcopy(hajoklista1)  # mélymásolat készítése
hajoklista2 = copy.deepcopy(hajoklista2)  # mélymásolat készítése
vaszontabla1 = [list(i) for i in tabla]  # alap tabla copy amin a tippek fognak látszani
vaszontabla2 = [list(i) for i in tabla]  # alap tabla copy amin a tippek fognak látszani
tippek1, tippek2 = [], []  # külön gyűjtjük a játékosok tippeit, jótippeit
jotippek1, jotippek2 = [], []  # külön gyűjtjük a játékosok tippeit, jótippeit


def jo_vagy_nem(jatekos: str, hajo: list, vaszontabla: list, tabla: list,
                tippek: list, bemenetikoordinata: str) -> str:
    """Ez a függvény a hajók betippelésénél a koordinátát vizsgálja, hogy az \
    az utasításnak megfelelően lett e megadva, ha igen módosítja a táblát \
    és a hajólistaszótárt, kigyűjti az aktuális adatokat, és visszatér azokkal"""
    try:
        x_ko, y_ko = bemenetikoordinata[0].upper(), bemenetikoordinata[1]
    except IndexError:
        return f"Hiba: string index out of range. A koordinátának legalább 2 karakterből kell\
        állnia. {bemenetikoordinata}, {len(bemenetikoordinata)}"

    if len(bemenetikoordinata) != 2 or x_ko not in "ABCDEFGHIJ" or y_ko not in \
     "0123456789":
        return "\nA-tól J-ig, 0-9-ig lehet megadni koordinétát, pl A0 vagy J9 "

    if bemenetikoordinata.upper() in tippek:
        return "\nEzt már tippelted, tippelj újra\n"

    ytengely, xtengely = int("ABCDEFGHIJ".index(x_ko)), int(y_ko)

    if tabla[ytengely][xtengely + 1] != "X":
        vaszontabla[ytengely][xtengely + 1] = "#"
        return "\nNem talált\n"

    vaszontabla[ytengely][xtengely + 1] = "X"

    for i in hajo:
        if bemenetikoordinata.upper(
        ) in i['koordinatak'] and i['megsemmisulte'] == 0:
            i['eltaltkoordinatak'].append(bemenetikoordinata.upper())
            hossz = 0
            eltalaltak = 0
            eltalaltkoordinatak = []
            printelendo = ""

            hossz = i['hajoHossz']
            eltalaltak = len(i['eltaltkoordinatak'])
            eltalaltkoordinatak = i['eltaltkoordinatak']

            printelendo = f"\nEltaláltad, lövés koordinata: {bemenetikoordinata}\n\n"
            printelendo += f"Az eltálalált hajó hossza: {hossz}\n"
            printelendo += f"Ennyit találtál el belőle: {eltalaltak}\n"
            printelendo += f"Ezeket a koordinátákat találtad el: {eltalaltkoordinatak}\n"
            if eltalaltak < hossz:
                return printelendo
            else:
                i['megsemmisulte'] += 1
                printelendo += "\nTalált süllyedt.\nA teljes hajó megsemmisült"
                return printelendo

    return "SEMMI"


def jatektablamegejlenito() -> None:
    """Ez a függvény megjeleníti a módosított, aktuális táblákat"""
    print(elso, "                            ", masodik)
    print()
    for k, v in zip(vaszontabla1, vaszontabla2):
        print(*k, "            ", *v)
    print()
    # print(elso, "                            ", masodik)
    # print()
    # for k, v in zip(tabla1, tabla2):
    #     print(*k, "            ", *v)
    # print()


def parbaly(jatekos: str, hajo: list, vaszontabla: list, tabla: list, tippek: list) -> \
str:
    """Ez a függvény kéri be a játékosoktól a koordinátákat, majd \
    átadja a többi függvénynek az aktuális paraméterekt, és rögzít minden \
    tippet, külön jó tippeket is."""
    tippeld = input(f"\n{jatekos} tippeld meg a koordinátát: ")
    os.system("clear")
    talalate = jo_vagy_nem(jatekos, hajo, vaszontabla, tabla, tippek, tippeld)
    jatektablamegejlenito()
    if "Eltaláltad" in talalate or "Nem talált" in talalate:
        tippek.append(tippeld.upper())

    if jatekos == elso and "Eltaláltad" in talalate:
        jotippek1.append(tippek[-1].upper())

    if jatekos == masodik and "Eltaláltad" in talalate:
        jotippek2.append(tippek[-1].upper())
    return talalate


while True:
    """Itt zajlik a felváltva való tippelés"""
    while True:
        tippek = []
        tippek = tippek1
        parbalyok = parbaly(elso, hajoklista2, vaszontabla2, tabla2, tippek1)
        print(parbalyok)

        if "Eltaláltad," in str(parbalyok) or "Nem talált" in str(parbalyok):
            break

    if len(jotippek2) == 21 or len(jotippek1) == 21:
        time.sleep(2)
        break

    while True:
        tippek = []
        tippek = tippek2
        parbalyok = parbaly(masodik, hajoklista1, vaszontabla1, tabla1,
                            tippek2)

        print(parbalyok)

        if "Eltaláltad," in str(parbalyok) or "Nem talált" in str(parbalyok):
            break

    if len(jotippek2) == 21 or len(jotippek1) == 21:
        time.sleep(2)
        break

print(f"{elso} a győztes" if len(jotippek1) == 21 else f"{masodik} a győztes")

for k, v in zip(tabla1, tabla2):
    print(*k, "            ", *v)