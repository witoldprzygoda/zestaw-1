import sys

# Funkcja do rozkładania liczby na czynniki pierwsze i formatowania wyniku
def rozklad_na_czynniki(n):
    pass  # zwrócić sformatowany ciąg, np. "2^3*3^4*5^2"

# Główna funkcja programu
if __name__ == "__main__":
    argv = sys.argv[1:]  # Pobieranie argumentów zewnętrznych (liczby)

    for arg in argv:
        liczba = int(arg)
        wynik = rozklad_na_czynniki(liczba)
        print(f"{liczba} = {wynik}")
