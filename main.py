from sklad import Sklad
from historie_skladu import HistorieSkladu

# Vytvoření instancí skladu a historie
sklad = Sklad()
historie_skladu = HistorieSkladu()

# Funkce pro zadávání číselných hodnot
def zadej_cislo(vyzva, typ=int):
    # Smyčka pro získání platného číselného vstupu od uživatele
    while True:
        try:
            return typ(input(vyzva))
        except ValueError:
            print("Chyba: Zadejte prosím platné číslo.")

# Hlavní smyčka programu pro interakci s uživatelem
while True:
    # Zobrazení hlavního menu
    print("\nMenu správy skladu:\n1. Přidat zboží\n2. Odebrat zboží\n3. Zobrazit stav skladu\n4. Zobrazit historii skladu\n5. Konec")
    volba = input("Vyberte akci (1-5): ")

    if volba == "1":
        # Smyčka pro přidání zboží
        while True:
            nazev = input("Zadejte název zboží: ")
            mnozstvi = zadej_cislo("Zadejte množství zboží k přidání: ")
            cena_za_kus = zadej_cislo("Zadejte cenu zboží v Kč: ", float)

            # Přidání zboží do skladu a do historie
            sklad.pridat_zbozi(nazev, mnozstvi, cena_za_kus)
            historie_skladu.pridej_polozku(nazev, mnozstvi, cena_za_kus)
            print(f"{mnozstvi} ks zboží '{nazev}' bylo přidáno. Cena za kus: {cena_za_kus} Kč, Celková cena: {mnozstvi * cena_za_kus} Kč.")

            # Možnost přidat další položku nebo se vrátit do menu
            while True:
                dalsi_akce = input("Pro přidání další položky stiskněte Enter, pro návrat do menu stiskněte 'M': ").lower()
                if dalsi_akce in ['', 'm']:
                    break
                print("Neplatný vstup. Zadejte prosím buď Enter pro pokračování nebo 'M' pro návrat do menu.")
            if dalsi_akce == 'm':
                break

    # Volba 2: Odebrání zboží
    elif volba == "2":
        # Smyčka pro odebrání zboží
        while True:
            sklad.zobraz_nabidku_zbozi()

            # Umožní uživateli vybrat zboží k odebrání nebo se vrátit zpět do menu
            vyber = zadej_cislo("Vyberte zboží k odebrání (číslo) nebo zadejte 'M' pro návrat do menu: ")
            if vyber == 'm':
                break

            # Kontroluje, zda je vybrané číslo platné
            if 1 <= vyber <= len(sklad.zbozi_slovnik):
                nazev = list(sklad.zbozi_slovnik.keys())[vyber - 1]
                mnozstvi = zadej_cislo(f"Zadejte množství zboží k odebrání (max {sklad.zbozi_slovnik[nazev].mnozstvi} ks): ")

                # Odebrání zboží a získání výsledku
                cena, zprava = sklad.odebrat_zbozi(nazev, mnozstvi)
                print(zprava)

                # Přidání transakce do historie, pokud nebyla vrácena žádná chyba
                if cena is not None:
                    historie_skladu.odeber_polozku(nazev, mnozstvi, cena / mnozstvi)
            else:
                print("Chyba: Neplatný výběr.")

            # Možnost odebrat další položku nebo se vrátit do menu
            while True:
                dalsi_akce = input("Pro odebrání další položky stiskněte Enter, pro návrat do menu stiskněte 'M': ").lower()
                if dalsi_akce in ['', 'm']:
                    break
                print("Neplatný vstup. Zadejte prosím buď Enter pro pokračování nebo 'M' pro návrat do menu.")

            if dalsi_akce == 'm':
                break

    # Volba 3: Zobrazení stavu skladu
    elif volba == "3":
        sklad.zobraz_stav()

    # Volba 4: Zobrazení historie skladu
    elif volba == "4":
        historie_skladu.zobraz_historii()

    # Volba 5: Ukončení programu
    elif volba == "5":
        print("Děkujeme za použití programu. Ukončuji...")
        break

    else:
        print("Chyba: Zadejte platnou volbu (1-5).")
