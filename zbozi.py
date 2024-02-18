# Definice třídy Zbozi
class Zbozi:
    def __init__(self, nazev, mnozstvi, cena_za_kus):
        # Inicializace instance třídy s názvem, množstvím a cenou za kus
        self.nazev = nazev
        self.mnozstvi = mnozstvi
        self.cena_za_kus = cena_za_kus

    def pridej_mnozstvi(self, mnozstvi):
        # Přidává zadané množství k množství zboží na skladě
        self.mnozstvi += mnozstvi

    def odeber_mnozstvi(self, mnozstvi):
        # Odebírá zadané množství z množství zboží na skladě, pokud je to možné
        if self.mnozstvi >= mnozstvi:
            self.mnozstvi -= mnozstvi

    def celkova_cena(self):
        # Vypočítává celkovou cenu zboží na skladě (množství * cena za kus)
        return self.mnozstvi * self.cena_za_kus
