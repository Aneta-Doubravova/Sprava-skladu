from zbozi import Zbozi

class Sklad:
    def __init__(self):
        # Inicializace slovníku pro uchovávání zboží
        self.zbozi_slovnik = {}

    def pridat_zbozi(self, nazev, pocet, cena_za_kus):
        # Přidává zboží do skladu. Pokud zboží již existuje, zvyšuje jeho množství
        if not isinstance(nazev, str) or not isinstance(pocet, int) or not isinstance(cena_za_kus, (float, int)):
            raise ValueError("Chyba: Neplatné vstupy.")

        nazev = nazev.lower()
        if nazev in self.zbozi_slovnik:
            # Zvýšení množství existujícího zboží
            self.zbozi_slovnik[nazev].pridej_mnozstvi(pocet)
        else:
            # Vytvoření nové instance zboží
            self.zbozi_slovnik[nazev] = Zbozi(nazev, pocet, cena_za_kus)

    def odebrat_zbozi(self, nazev, pocet):
        # Odebírá zboží ze skladu. Pokud je počet větší než množství na skladě, vrací chybu
        if not isinstance(nazev, str) or not isinstance(pocet, int):
            raise ValueError("Chyba: Neplatné vstupy.")

        nazev = nazev.lower()
        if nazev in self.zbozi_slovnik:
            existujici_zbozi = self.zbozi_slovnik[nazev]
            if pocet > existujici_zbozi.mnozstvi:
                return None, f"Chyba: Nelze odebrat, na skladě je pouze {existujici_zbozi.mnozstvi} ks."
            else:
                cena = existujici_zbozi.cena_za_kus * pocet
                existujici_zbozi.odeber_mnozstvi(pocet)
                if existujici_zbozi.mnozstvi == 0:
                    del self.zbozi_slovnik[nazev]
                    return cena, f"Zboží '{nazev}' bylo odebráno ve množství {pocet} ks. Cena celkem: {cena} Kč. Zboží již není skladem."
                else:
                    return cena, f"{pocet} ks zboží '{nazev}' bylo odebráno. Cena celkem: {cena} Kč."
        else:
            return None, "Chyba: Zboží s tímto názvem není na skladě."
    def zobraz_nabidku_zbozi(self):
        # Zobrazuje seznam zboží dostupného k odebrání ze skladu
        if not self.zbozi_slovnik:
            print("Na skladě není žádné zboží k odebrání.")
            return

        print("\nSeznam zboží k odebrání:")
        for cislo, (nazev, zbozi) in enumerate(self.zbozi_slovnik.items(), start=1):
            print(f"{cislo}. {nazev} - množství: {zbozi.mnozstvi}, cena za kus: {zbozi.cena_za_kus} Kč")

    def zobraz_stav(self):
        # Zobrazuje celkový stav zboží na skladě včetně celkového počtu a hodnoty
        if not self.zbozi_slovnik:
            print("Na skladě není žádné zboží.")
            return

        print("\nStav skladu:")
        celkove_mnozstvi = 0
        celkova_cena = 0
        for nazev, zbozi in self.zbozi_slovnik.items():
            print(
                f"{nazev}: {zbozi.mnozstvi} ks, Cena za kus: {zbozi.cena_za_kus} Kč, Cena celkem: {zbozi.celkova_cena()} Kč")
            celkove_mnozstvi += zbozi.mnozstvi
            celkova_cena += zbozi.celkova_cena()

        print(f"\nCelkem položek: {celkove_mnozstvi} ks, Celková hodnota: {celkova_cena} Kč")

