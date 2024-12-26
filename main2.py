import os
class Torpedeo:
    def __init__(self, tabla):
        self.tabla = [["A)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
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
        self.titoktabla = [["A)", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
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
        self.hajoklista = [{
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
        self.letett_hajok_szama = sum(1 for i in self.hajoklista if i["ennyiVan"] == 1)
        self.hajokoordinatai = set()
        self.hajok_melletti_koordinatak = set()
        self.tippelt_cellak = []
        self.eltalalt_hajok_szama = 0
        self.nev = ""

    def tabla_megjelenites(self, tabla):
        "Megjeleníti a táblát"
        [print(*j) for j in tabla]

    def hajo_bekeres(self):
        "Bekéri a játékostól a hajó kezdőkoordinátáját"
        print("Add meg a hajó kezdő koordinátáját (A-J-ig és 0-9-ig Pl A0 vagy J9) ")
        kezdokordinata = input("Kezdő koordináta: ").upper()
        return kezdokordinata

    def irany_bekeres(self):
        "Bekéri a játékostól az irányt"
        print("Add meg a hajó irányt (É/K/NY/D):")
        irany = input("Irány: ").upper()
        return irany

    def iranyellenorzo(self, irany):
        "Ez a függvény, ellenőrzi, hogy amennyiben szükséges megadni irányt, jól adta e meg az irányt a felhasználó."
        match irany.upper():
            case "É":
                return True
            case "D":
                return True
            case "NY":
                return True
            case "K":
                return True
            case other:
                return False

    def sor_oszlop_ellenorzes(self, sor, oszlop):
        "Ellenőrzi, hogy a kezdő koordináta pályán belül van e"
        return sor in "ABCDEFGHIJ" and oszlop in "0123456789"

    def kiszamol(self, sor, oszlop, hossz, irany):
        "Kiszámolja a hajó további koordinátáit"
        if hossz > 1:
            sor, oszlop = ord(sor.upper()) - ord('A'), int(oszlop)
            koordinatak = [(sor, oszlop)]
            iranyok = {
                "É": (-1, 0),
                "D": (1, 0),
                "K": (0, 1),
                "NY": (0, -1)
            }
            for _ in range(int(hossz)-1):
                x,y = (koordinatak[-1])
                koordinatak.append((x+iranyok[irany][0], y+iranyok[irany][1]))
            return [(chr(ord('A') + x) + str(y)) for x, y in koordinatak]
        else:
            return  [sor + str(oszlop)]

    def hajo_melletti_kordinatak(self, koordinatak):
        "Kiszámolja a hajó mellett lévő koordinátákat"
        mellettikord = set()
        pontok = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1),
              (1, 1)]
        
        for betu, szam in koordinatak:
            szam = int(szam)
            for pont in pontok:
                if 0 <= ord(betu)-ord("A") + pont[0] < 10 and 0 <= szam + pont[1] < 10:
                    mellettikord.add(
                        chr(ord(betu) + pont[0]) + str(szam + pont[1]))
            
        return mellettikord - set(koordinatak)
        
    def utkozes_ellenorzo(self, hajokoordinatak):
        "Ellenőrzi, hogy nem e ütközik más hajóval/nincs mellette közvetlen más hajó"
        hajokoordinatak = set(hajokoordinatak) 
        if hajokoordinatak & self.hajokoordinatai:
            return False
        if hajokoordinatak & self.hajok_melletti_koordinatak:
            return False
        return True

    def palyan_beluli_ellenorzes(self, hajokoordinatak):
        "Ellenőrzi, hogy a hajó összes koordinátája pályán belül van e"
        for i in hajokoordinatak:
            x, y = i[0], i[1:]
            if not (x in "ABCDEFGHIJ" and y in "0123456789"):
                return False
        return True

    def hajoellenorzes(self, kezdokoordinata, hossz, irany=None):
        "Ellenőrzi a megadott hajót, ha nem felel meg, hibát dob, ellenben vissza adja a hajó koordinátáit."
        if len(kezdokoordinata) != 2:
            raise ValueError("A kezdőkoordináta csak 2 elemből állhat egy betűből(A-J) és egy számból (0-9)")
        sor = kezdokoordinata[0]
        oszlop = kezdokoordinata[1]
        if not self.sor_oszlop_ellenorzes(sor, oszlop):
            raise ValueError("A kezdő koordináta érvénytelen! Csak A-J és 0-9 értékek engedélyezettek.")

        elif not self.iranyellenorzo(irany):
            raise ValueError("Az irány érvénytelen! Csak É/D/K/NY engedélyezettek.")

        else:
            hajokoordinatak = self.kiszamol(sor, oszlop, hossz, irany)        
        
            if not self.palyan_beluli_ellenorzes(hajokoordinatak):
                raise ValueError("A hajó egy vagy több része a pályán kívülre esik!")
            
            if not self.utkozes_ellenorzo(hajokoordinatak):
                raise ValueError("A hajó ütközik egy másik hajóval, vagy túl közel van hozzá.")
            
            return hajokoordinatak

    def hajoelhelyezes(self, hajokoordinatak):
        "Ez a függvény elhelyezi a táblán az új hajót"
        for i in hajokoordinatak:
            x,y = int(i[1])+1, ord(i[0]) - ord('A')
            self.tabla[y][x] = "X"
            
    def hajokord_es_hajokordmelletti(self, hajokoordinatak):
        "Rögzíti az új hajó koordinátáját és a mellette lévő koordinátákat"
        self.hajok_melletti_koordinatak.update(self.hajo_melletti_kordinatak(hajokoordinatak))
        self.hajokoordinatai.update(hajokoordinatak)
        
    def hajoklistamodosito(self, hanyadikhajo, hajokoordinatak):
        "Itt módosítjuk az összes hajó tulajdonságait, pl belerakjuk a koordinatait, és a mellette lévő koordinátákat"
        self.hajoklista[hanyadikhajo-1]["koordinatak"] = hajokoordinatak
        self.hajoklista[hanyadikhajo-1]["mellettekord."] = self.hajo_melletti_kordinatak(hajokoordinatak)

    def tippbekero(self, nev):
        "Bekéri a tippeket"
        tipp = input(f"{nev}: Hova lősz?: ").upper()
        return tipp

    def  tippellenorzo(self, tipp, tippjeid):
        "Ellenőrzi a tippet, visszatér az eredménnyel"
        if len(tipp) != 2:
            raise ValueError("2 elemből kell állnia a tippnek, egy betűből (A-J) és egy számól (0-9)")
        if not self.sor_oszlop_ellenorzes(tipp[0].upper(), tipp[1].upper()):
            raise ValueError("A-J között és 0-9 között add meg a koordinátát, pl A0 vagy J9")
        if tipp in tippjeid:
            raise ValueError("Ezt már tippelted...")
        return True

    def hajomodositasok(self, tipp, egyik, masik):
        "Módodosítja azt amit kell"
        egyik.tippelt_cellak.append(tipp)
        x,y = int(tipp[1])+1, ord(tipp[0]) - ord('A')
        if tipp in masik.hajokoordinatai:
            for i in masik.hajoklista:
                if tipp in i["koordinatak"]:
                    i["eltaltkoordinatak"].append(tipp)
                    masik.titoktabla[y][x] = "X"
                    szoveg = f"""\033[32m
Eltaláltad, lövés koordinata: {tipp}
Az eltálalált hajó hossza: {i["hajoHossz"]}
Ennyit találtál el belőle: {len(i["eltaltkoordinatak"])}
Ezeket a koordinátákat találtad el: {i["eltaltkoordinatak"]}\033[0m
                            """
                    if len(i["koordinatak"]) == len(i["eltaltkoordinatak"]):
                        egyik.eltalalt_hajok_szama += 1
                        szoveg += "\033[32mTalált süllyedt. \nA teljes hajó megsemmisült \033[0m"
                    self.tablakmegjelenitese(egyik.titoktabla, masik.titoktabla, egyik.nev, masik.nev)
                    return szoveg
        else:
            masik.titoktabla[y][x] = "#"
            self.tablakmegjelenitese(egyik.titoktabla, masik.titoktabla, egyik.nev, masik.nev)
            return "Nem talált"

    def tablakmegjelenitese(self, tabla1, tabla2, nev1, nev2):
        "Megjeleníti a táblákat, és a hozzájuk tartozó neveket"
        print(f"{nev1}\t\t\t\t\t{nev2}")
        for k, v in zip(tabla1, tabla2):
            print(*k, "            ", *v)
        

player1 = Torpedeo(None)
player2 = Torpedeo(None)
playerek = [player1, player2]
for player in playerek:
    os.system("cls")
    player.nev = input("Add meg a neved: ")
    player.tabla_megjelenites(player.tabla)
    for i, hajo in enumerate(player.hajoklista, start=1):  # Hajók listájának végigjárása
        while True:  # Addig ismétel, amíg sikeresen el nem helyezi a hajót
            try:
                # player.tabla_megjelenites(player.tabla)
                print(f"{player.nev} add meg a hajóid")
                print(f"\nHelyezd el a(z) {i}. hajót! Hossz: {hajo['hajoHossz']} mező")
                kezdokoordinata = player.hajo_bekeres()        
                if hajo['hajoHossz'] != 1: 
                    irany = player.irany_bekeres() 
                hajokoordinatak = player.hajoellenorzes(kezdokoordinata, hajo["hajoHossz"], irany)
                player.hajoelhelyezes(hajokoordinatak)
                player.hajokord_es_hajokordmelletti(hajokoordinatak)
                player.hajoklistamodosito(i, hajokoordinatak)
                
                os.system("cls")
                player1.tabla_megjelenites(player.tabla)
                print("\033[32m Hajó sikeresen elhelyezve! \033[0m")
                break
            except ValueError as e:
                os.system("cls")
                player1.tabla_megjelenites(player.tabla)
                print(f"\033[31m Hiba: {e} \033[0m")
os.system("cls")
player1.tablakmegjelenitese(player1.titoktabla, player2.titoktabla, player1.nev, player2.nev)
jatekosvalaszto = 0
while True:
    egyik = playerek[jatekosvalaszto % 2]
    masik = playerek[(jatekosvalaszto % 2)-1]
    try:
        while True:
            
            tipp = egyik.tippbekero(egyik.nev)
            if egyik.tippellenorzo(tipp, egyik.tippelt_cellak):
                os.system("cls")
                print(egyik.hajomodositasok(tipp, egyik, masik))
                jatekosvalaszto += 1
                break
    except ValueError as e:
        os.system("cls")
        egyik.tablakmegjelenitese(player1.titoktabla, player2.titoktabla, player1.nev, player2.nev)
        print(f"\033[31m Hiba: {e} \033[0m")

    if egyik.eltalalt_hajok_szama == 6:
        print(f"\033[31mA győztes: {egyik.nev}\033[0m")
        print("ITT voltak a hajók:")
        egyik.tablakmegjelenitese(player1.tabla, player2.tabla, player1.nev, player2.nev)
        break
