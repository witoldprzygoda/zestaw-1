import requests

MIASTA = [
    ("Warszawa","Warszawa"),("Kraków","Krakow"),("Łódź","Lodz"),("Wrocław","Wroclaw"),
    ("Poznań","Poznan"),("Gdańsk","Gdansk"),("Szczecin","Szczecin"),("Bydgoszcz","Bydgoszcz"),
    ("Lublin","Lublin"),("Białystok","Bialystok"),("Katowice","Katowice"),("Gdynia","Gdynia"),
    ("Częstochowa","Czestochowa"),("Radom","Radom"),("Toruń","Torun"),
]

# Należy zdefiniować funkcję skaner_temperatur(), która zwraca listę krotek (miasto, temperatura_int)
# w tej samej kolejności co MIASTA. Źródłem danych jest serwis wttr.in (adres: https://wttr.in/NazwaMiasta?format=j1).
# Funkcja ma pobrać bieżącą temperaturę w °C (klucz "temp_C"), zamienić ją na int i zbudować listę wyników.
#
# Oczekiwane użycie w programie:
# - wywołanie skaner_temperatur(), wypisanie zestawienia "Miasto : temperatura °C" w oddzielnych liniach,
# - wyznaczenie miasta z najniższą i najwyższą temperaturą (nazwy i wartości) na podstawie zwróconej listy,
# - przypisanie wyników do zmiennych: min_miasto, min_temp, max_miasto, max_temp.

if __name__ == "__main__":
    # twoj kod

    print("\n=== Podsumowanie ===")
    print("Najchłodniej:", min_miasto, ": ", min_temp, "°C")
    print("Najcieplej: ", max_miasto, ": ", max_temp, "°C")
