class HistorieSkladu:
    def __init__(self):
        # Inicializace seznamu pro historii a slovníku pro aktuální stav
        self.historie = []
        self.aktualni_stav = {"Přidáno": {"Počet": 0, "Cena celkem": 0.0}, "Odebráno": {"Počet": 0, "Cena celkem": 0.0}}

    def pridej_polozku(self, nazev, pocet, cena_za_kus):
        # Přidává položku do historie při přidání zboží a aktualizuje stav
        cena_celkem = pocet * cena_za_kus
        self.historie.append(f"Přidáno: {nazev}, Počet: {pocet}, Cena za kus: {cena_za_kus} Kč, Cena celkem: {cena_celkem} Kč")
        self.aktualni_stav["Přidáno"]["Počet"] += pocet
        self.aktualni_stav["Přidáno"]["Cena celkem"] += cena_celkem

    def odeber_polozku(self, nazev, pocet, cena_za_kus):
        # Přidává položku do historie při odebírání zboží a aktualizuje stav
        cena_celkem = pocet * cena_za_kus
        self.historie.append(f"Odebráno: {nazev}, Počet: {pocet}, Cena za kus: {cena_za_kus} Kč, Cena celkem: {cena_celkem} Kč")
        self.aktualni_stav["Odebráno"]["Počet"] += pocet
        self.aktualni_stav["Odebráno"]["Cena celkem"] += cena_celkem

    def zobraz_historii(self):
        # Zobrazuje kompletní historii transakcí skladu
        print("\nHistorie skladu:")
        for polozka in self.historie:
            if not polozka.startswith("Celkem "):  # Tímto způsobem přeskočíme řádky s celkovým souhrnem
                print(polozka)

        # Výpis celkového souhrnu na konci
        pocet_pridano, cena_pridano = self.souhrn_pridano()
        pocet_odebrano, cena_odebrano = self.souhrn_odebrano()
        print(f"\nCelkem přidáno položek zboží: {pocet_pridano}, Cena celkem: {cena_pridano:.2f} Kč")
        print(f"Celkem odebráno položek zboží: {pocet_odebrano}, Cena celkem: {cena_odebrano:.2f} Kč")

    def souhrn_stavu(self):
        # Vrací celkový souhrn přidaného a odebraného zboží
        pocet_pridano = self.aktualni_stav["Přidáno"]["Počet"]
        cena_pridano = self.aktualni_stav["Přidáno"]["Cena celkem"]
        pocet_odebrano = self.aktualni_stav["Odebráno"]["Počet"]
        cena_odebrano = self.aktualni_stav["Odebráno"]["Cena celkem"]
        return [pocet_pridano, cena_pridano, pocet_odebrano, cena_odebrano]

    def souhrn_pridano(self):
        # Vrací souhrn pouze přidaného zboží
        pocet_pridano = self.aktualni_stav["Přidáno"]["Počet"]
        cena_pridano = self.aktualni_stav["Přidáno"]["Cena celkem"]
        return pocet_pridano, cena_pridano

    def souhrn_odebrano(self):
        # Vrací souhrn pouze odebraného zboží
        pocet_odebrano = self.aktualni_stav["Odebráno"]["Počet"]
        cena_odebrano = self.aktualni_stav["Odebráno"]["Cena celkem"]
        return pocet_odebrano, cena_odebrano
