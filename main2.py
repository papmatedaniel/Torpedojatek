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

    def hajo_bekeres(self):
        "Bekéri a játékostól a hajókat"
        print("Add meg a hajó kezdő koordinátáját (A-J-ig és 0-9-ig Pl A0 vagy J9) és az irányt (É/K/NY/D):")
        adat = input("Kezdő koordináta és irány: ").upper()
        return adat

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
        if len(hajokoordinatak & self.hajokoordinatai) > 0:
            return False
        if len(hajokoordinatak & self.hajok_melletti_koordinatak) > 0:
            return False
        return True

    def palyan_beluli_ellenorzes(self, hajokoordinatak):
        "Ellenőrzi, hogy a hajó összes koordinátája pályán belül van e"
        for i in hajokoordinatak:
            x, y = i[0], i[1:]
            if not (x in "ABCDEFGHIJ" and y in "0123456789"):
                return False
        return True

    def hajoellenorzes(self, sor, oszlop, hossz, irany=None):
        "Ellenőrzi a megadott hajót, ha nem felel meg, hibát dob, ellenben vissza adja a hajó koordinátáit."
        hajokoordinatak = self.kiszamol(sor, oszlop, hossz, irany)
        if not self.sor_oszlop_ellenorzes(sor, oszlop):
            raise ValueError("A kezdő koordináta érvénytelen! Csak A-J és 0-9 értékek engedélyezettek.")
        
        
        elif not self.palyan_beluli_ellenorzes(hajokoordinatak):
            raise ValueError("A hajó egy vagy több része a pályán kívülre esik!")
        
        elif not self.utkozes_ellenorzo(hajokoordinatak):
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


player1 = Torpedeo(None)

# Hajók elhelyezése
for i, hajo in enumerate(player1.hajoklista, start=1):  # Hajók listájának végigjárása
    while True:  # Addig ismétel, amíg sikeresen el nem helyezi a hajót
        try:
            print(f"\nHelyezd el a(z) {i}. hajót! Hossz: {hajo['hajoHossz']} mező")
            adat = player1.hajo_bekeres()
            
            # Bevitt adat feldolgozása
            kezdosor, kezdoszlop = adat[0], adat[1]#itt hiba ha csak 1 hosszú a hajó!!!
            if hajo['hajoHossz'] != 1:
               irany = adat.split()[1]
            
            # Hajó koordinátáinak ellenőrzése
            hajokoordinatak = player1.hajoellenorzes(kezdosor, kezdoszlop, hajo["hajoHossz"], irany)
            
            # Hajó elhelyezése
            player1.hajoelhelyezes(hajokoordinatak)
            
            # Hajók koordinátáinak és mellékkoordinátáinak mentése
            player1.hajokord_es_hajokordmelletti(hajokoordinatak)
            
            # Hajó lista frissítése
            player1.hajoklistamodosito(i, hajokoordinatak)
            
            # Sikeres elhelyezés után kilépés a ciklusból
            print("Hajó sikeresen elhelyezve!")
            for i in player1.tabla:
                print(*i)
            break
        except ValueError as e:
            # Ha bármelyik ellenőrzés hibát jelez, újra bekérjük az adatokat
            print(f"Hiba: {e}")

