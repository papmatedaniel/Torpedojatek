import os
import random


class Hajo:
    def __init__(self, hossz: int):
        self.hossz = hossz
        self.megsemmisulte = 0
        self.eltalaltkoordinatak = []
        self.koordinatak = []
        self.mellettekord = []


class Torpedeo:
    def __init__(self):
        self.tabla = self.uj_tabla()
        self.titoktabla = self.uj_tabla()
        self.hajoklista = self.hajok_lista()
        self.hajokoordinatai = set()
        self.hajok_melletti_koordinatak = set()
        self.tippelt_cellak = []
        self.eltalalt_hajok_szama = 0
        self.nev = ""

    def hajok_lista(self) -> list[Hajo(int)]:
        """Létrehozza és feltölti Hajó objektumokkal a listát, amellyel visszatér"""
        random.shuffle(lista := list(range(1, 7)))
        return [Hajo(i) for i in lista]

    def uj_tabla(self) -> list[list[str]]:
        """Új táblát hoz létre"""
        return [["." for _ in range(10)] for _ in range(10)]

    def tabla_megjelenites(self, tabla: list[list[str]]) -> None:
        """Megjeleníti a táblát"""
        sorbetuk = "ABCDEFGHIJ"
        [print(sorbetuk[i] + ")", *tabla[i]) for i in range(len(tabla))]
        print("   0 1 2 3 4 5 6 7 8 9")
    
    def nevbeker(self, nev1, nev2) -> str:
        '''Bekéri a neveket a játékosoktól'''
        while True:
            nev = input("Add meg a neved. (2-7) karakter hosszúságban: ")
            if 2 > len(nev) or len(nev) > 7:
                print("2-7 karakter hossszú nevet válassz!")
            elif nev1 == nev or nev2 == nev:
                print("Ne ugyanazt a nevet add meg mint a másik játékos")
            else:
                return nev


    def hajo_bekeres(self) -> str:
        """Bekéri a játékostól a hajó kezdőkoordinátáját"""
        print("Add meg a hajó kezdő koordinátáját (A-J-ig és 0-9-ig Pl A0 vagy J9) ")
        kezdokordinata = input("Kezdő koordináta: ").upper()
        return kezdokordinata

    def irany_bekeres(self) -> str:
        """Bekéri a játékostól az irányt"""
        print("Add meg a hajó irányt (É/K/NY/D):")
        irany = input("Irány: ").upper()
        return irany

    def iranyellenorzo(self, irany: str) -> bool:
        """Ez a függvény, ellenőrzi, hogy amennyiben szükséges megadni irányt, jól adta e meg az irányt a felhasználó."""
        match irany.upper():
            case "É":
                return True
            case "D":
                return True
            case "NY":
                return True
            case "K":
                return True
            case _:
                return False

    def sor_oszlop_ellenorzes(self, sor: str, oszlop: str) -> bool:
        """Ellenőrzi, hogy a kezdő koordináta pályán belül van e"""
        return sor in "ABCDEFGHIJ" and oszlop in "0123456789"

    def kiszamol(self, sor: str, oszlop: str, hossz: int, irany: str) -> list[str]:
        """Kiszámolja a hajó további koordinátáit"""
        sor, oszlop = "ABCDEFGHIJ".index(sor.upper()), int(oszlop)
        koordinatak = [(oszlop, sor)]
        if hossz > 1:
            iranyok = {"É": (0, -1), "D": (0, 1), "K": (1, 0), "NY": (-1, 0)}
            for _ in range(int(hossz) - 1):
                x, y = koordinatak[-1]
                koordinatak.append((x + iranyok[irany][0], y + iranyok[irany][1]))
            return [(x, y) for x, y in koordinatak]
        else:
            return koordinatak

    def hajo_melletti_kordinatak(
        self, koordinatak: list[tuple[int, int]]
    ) -> set[tuple[int, int]]:
        """Kiszámolja a hajó mellett lévő koordinátákat"""
        mellettikord = set()
        pontok = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1), (1, 1)]

        for x, y in koordinatak:
            for pont in pontok:
                if 0 <= x + pont[0] < 10 and 0 <= y + pont[1] < 10:
                    mellettikord.add((x + pont[0], y + pont[1]))

        return mellettikord - set(koordinatak)

    def utkozes_ellenorzo(self, hajokoordinatak: list[str]) -> bool:
        """Ellenőrzi, hogy nem e ütközik más hajóval/nincs mellette közvetlen más hajó"""
        hajokoordinatak = set(hajokoordinatak)
        if hajokoordinatak & self.hajokoordinatai:
            return False
        if hajokoordinatak & self.hajok_melletti_koordinatak:
            return False
        return True

    def palyan_beluli_ellenorzes(self, hajokoordinatak: list[tuple[int, int]]) -> bool:
        """Ellenőrzi, hogy a hajó összes koordinátája pályán belül van e"""
        for i in hajokoordinatak:
            x, y = i[0], i[1]
            if not (0 <= x <= 9 and 0 <= y <= 9):
                return False
        return True

    def hajoellenorzes(
        self, kezdokoordinata: str, hossz: int, irany=None
    ) -> list[str] | ValueError:
        """Ellenőrzi a megadott hajót, ha nem felel meg, hibát dob, ellenben vissza adja a hajó koordinátáit."""
        if len(kezdokoordinata) != 2:
            raise ValueError(
                "A kezdőkoordináta csak 2 elemből állhat egy betűből(A-J) és egy számból (0-9)"
            )
        sor = kezdokoordinata[0]
        oszlop = kezdokoordinata[1]
        if not self.sor_oszlop_ellenorzes(sor, oszlop):
            raise ValueError(
                "A kezdő koordináta érvénytelen! Csak A-J és 0-9 értékek engedélyezettek."
            )

        elif hossz != 1 and not self.iranyellenorzo(irany):
            raise ValueError("Az irány érvénytelen! Csak É/D/K/NY engedélyezettek.")

        else:
            hajokoordinatak = self.kiszamol(sor, oszlop, hossz, irany)

            if not self.palyan_beluli_ellenorzes(hajokoordinatak):
                raise ValueError("A hajó egy vagy több része a pályán kívülre esik!")

            if not self.utkozes_ellenorzo(hajokoordinatak):
                raise ValueError(
                    "A hajó ütközik egy másik hajóval, vagy túl közel van hozzá."
                )

            return hajokoordinatak

    def hajoelhelyezes(self, hajokoordinatak: list[tuple[int, int]]) -> None:
        """Ez a függvény elhelyezi a táblán az új hajót"""
        for i in hajokoordinatak:
            x, y = i[0], i[1]
            self.tabla[y][x] = "X"

    def hajokord_es_hajokordmelletti(
        self, hajokoordinatak: list[tuple[int, int]]
    ) -> None:
        """Rögzíti az új hajó koordinátáját és a mellette lévő koordinátákat"""
        self.hajok_melletti_koordinatak.update(
            self.hajo_melletti_kordinatak(hajokoordinatak)
        )
        self.hajokoordinatai.update(hajokoordinatak)

    def hajoklistamodosito(
        self, hanyadikhajo: int, hajokoordinatak: list[tuple[int, int]]
    ) -> None:
        """Itt módosítjuk az összes hajó tulajdonságait, pl belerakjuk a koordinatait, és a mellette lévő koordinátákat"""
        self.hajoklista[hanyadikhajo - 1].koordinatak = hajokoordinatak
        self.hajoklista[hanyadikhajo - 1].mellettekord = self.hajo_melletti_kordinatak(
            hajokoordinatak
        )

    def tippbekero(self, nev: str) -> str:
        """Bekéri a tippeket"""
        tipp = input(f"{nev}: Hova lősz?: ").upper()
        return tipp

    def tippellenorzo(self, tipp: str, tippjeid: list[int]) -> bool | ValueError:
        """Ellenőrzi a tippet, visszatér az eredménnyel"""
        if len(tipp) != 2:
            raise ValueError(
                "2 elemből kell állnia a tippnek, egy betűből (A-J) és egy számól (0-9)"
            )
        if not self.sor_oszlop_ellenorzes(tipp[0].upper(), tipp[1].upper()):
            raise ValueError(
                "A-J között és 0-9 között add meg a koordinátát, pl A0 vagy J9"
            )
        if tipp in tippjeid:
            raise ValueError("Ezt már tippelted...")
        return True

    def hajomodositasok(self, tipp: str, egyik: object, masik: object) -> str:
        """Módosítja a tippek alapján a táblát, hajólistát, visszajelzést küld a tipp sikerességéről/sikertelenségéről"""
        egyik.tippelt_cellak.append(tipp)
        x, y = int(tipp[1]), ord(tipp[0]) - ord("A")
        tipp_tuple = (x, y)

        if tipp_tuple in masik.hajokoordinatai:
            for i in masik.hajoklista:
                if tipp_tuple in i.koordinatak:
                    i.eltalaltkoordinatak.append(tipp_tuple)
                    koordinatak_kiirasa = [
                        ("ABCDEFGHIJ"[x] + str(y)) for x, y in i.eltalaltkoordinatak
                    ]
                    masik.titoktabla[y][x] = "X"
                    szoveg = f"""\033[32m Eltaláltad, lövés koordinata: {tipp}
    Az eltálalált hajó hossza: {i.hossz}
    Ennyit találtál el belőle: {len(i.eltalaltkoordinatak)}
    Ezeket a koordinátákat találtad el: {koordinatak_kiirasa}\033[0m
                    """
                    if len(i.koordinatak) == len(i.eltalaltkoordinatak):
                        egyik.eltalalt_hajok_szama += 1
                        szoveg += "\033[32mTalált süllyedt. \nA teljes hajó megsemmisült \033[0m"
                    self.tablakmegjelenitese(
                        player1.titoktabla, player2.titoktabla, player1.nev, player2.nev
                    )
                    return szoveg
        else:
            masik.titoktabla[y][x] = "#"
            self.tablakmegjelenitese(
                player1.titoktabla, player2.titoktabla, player1.nev, player2.nev
            )
            return "Nem talált"

    def tablakmegjelenitese(
        self, tabla1: list[list[str]], tabla2: list[list[str]], nev1: str, nev2: str
    ):
        "Megjeleníti a táblákat, és a hozzájuk tartozó neveket"
        sorbetuk = "ABCDEFGHIJ"
        print(f"{nev1}\t\t\t\t\t{nev2}")
        for i in range(len(tabla1)):
            print(
                sorbetuk[i] + ")",
                *tabla1[i],
                "            ",
                sorbetuk[i] + ")",
                *tabla2[i],
            )
        print("   0 1 2 3 4 5 6 7 8 9")


player1 = Torpedeo()
player2 = Torpedeo()
print("1. Játékos:")
player1.nev = player1.nevbeker(player1.nev, player2.nev)
print("2. Játékos:")
player2.nev = player2.nevbeker(player1.nev, player2.nev)

playerek = [player1, player2]
for player in playerek:
    os.system("clear") | os.system("cls")
    
    player.tabla_megjelenites(player.tabla)
    for i, hajo in enumerate(
        player.hajoklista, start=1
    ):  # Hajók listájának végigjárása
        while True:  # Addig ismétel, amíg sikeresen el nem helyezi a hajót
            try:
                print(f"{player.nev} add meg a hajóid")
                print(f"\nHelyezd el a(z) {i}. hajót! Hossz: {hajo.hossz} mező")
                kezdokoordinata = player.hajo_bekeres()
                if hajo.hossz != 1:
                    irany = player.irany_bekeres()
                    hajokoordinatak = player.hajoellenorzes(
                        kezdokoordinata, hajo.hossz, irany
                    )
                else:
                    hajokoordinatak = player.hajoellenorzes(kezdokoordinata, hajo.hossz)

                player.hajoelhelyezes(hajokoordinatak)
                player.hajokord_es_hajokordmelletti(hajokoordinatak)
                player.hajoklistamodosito(i, hajokoordinatak)

                os.system("clear") | os.system("cls")
                player1.tabla_megjelenites(player.tabla)
                print("\033[32m Hajó sikeresen elhelyezve! \033[0m")
                break
            except ValueError as e:
                os.system("clear") | os.system("cls")
                player1.tabla_megjelenites(player.tabla)
                print(f"\033[31m Hiba: {e} \033[0m")
os.system("clear") | os.system("cls")
player1.tablakmegjelenitese(
    player1.titoktabla, player2.titoktabla, player1.nev, player2.nev
)
jatekosvalaszto = 0
while True:
    egyik = playerek[jatekosvalaszto % 2]
    masik = playerek[(jatekosvalaszto % 2) - 1]
    try:
        while True:
            tipp = egyik.tippbekero(egyik.nev)
            if egyik.tippellenorzo(tipp, egyik.tippelt_cellak):
                os.system("clear") | os.system("cls")
                print(egyik.hajomodositasok(tipp, egyik, masik))
                jatekosvalaszto += 1
                break
    except ValueError as e:
        os.system("clear") | os.system("cls")
        egyik.tablakmegjelenitese(
            player1.titoktabla, player2.titoktabla, player1.nev, player2.nev
        )
        print(f"\033[31m Hiba: {e} \033[0m")

    if egyik.eltalalt_hajok_szama == 6:
        print(f"\033[31mA győztes: {egyik.nev}\033[0m")
        print("ITT voltak a hajók:")
        egyik.tablakmegjelenitese(
            player1.tabla, player2.tabla, player1.nev, player2.nev
        )
        break
