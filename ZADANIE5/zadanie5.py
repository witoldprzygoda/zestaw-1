import requests

MODEL = "llama3.2:1b"          # np. `ollama pull llama3.2:1b`
URL   = "http://localhost:11434/api/generate"

def pobierz_odpowiedz(prompt):
    """
    Zwróć tekstową odpowiedź modelu na podany prompt.
    - Skorzystaj z biblioteki `requests` i wyślij żądanie POST pod lokalny adres API.
    - Przekaż model i treść promptu w formacie JSON.
    - Odbierz odpowiedź w formacie JSON i zwróć pole z wygenerowanym tekstem.
    - Funkcja ma zwracać `str`.
    """
    pass


def uruchom_czat():
    """
    Zaimplementuj pętlę czatu z obsługą zakończenia pustym ENTER-em.
    - W pętli pobieraj wejście użytkownika (`input()`).
    - Pusty wiersz ma zakończyć działanie czatu.
    - Dla każdej niepustej wypowiedzi wywołaj `pobierz_odpowiedz` i wypisz wynik w formacie: "Model: <odpowiedź>".
    """
    pass


if __name__ == "__main__":
    uruchom_czat()
