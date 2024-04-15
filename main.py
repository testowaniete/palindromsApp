def znajdz_najdluzszy_palindrom(ciag):
    n = len(ciag)
    
    # Funkcja sprawdzająca, czy dany fragment ciągu jest palindromem
    def jest_palindrom(s, start, koniec):
        while start < koniec:
            if s[start] != s[koniec]:
                return False
            start += 1
            koniec -= 1
        return True
    
    max_dlugosc = 0
    start_indeks = 0
    
    # Sprawdzanie każdej możliwej pary indeksów
    for i in range(n):
        for j in range(i + 1, n):
            dlugosc = j - i + 1
            
            # Jeśli aktualny fragment jest palindromem i jest dłuższy od dotychczasowego maksimum
            if jest_palindrom(ciag, i, j) and dlugosc > max_dlugosc:
                max_dlugosc = dlugosc
                start_indeks = i
    
    # Jeśli nie znaleziono żadnego palindromu
    if max_dlugosc == 0:
        return "brak"
    
    # Zwracanie najdłuższego palindromu
    return ciag[start_indeks:start_indeks + max_dlugosc]

# Przykłady użycia
print(znajdz_najdluzszy_palindrom("CABCBAB"))  # Powinno zwrócić "ABCBA"
print(znajdz_najdluzszy_palindrom("CABCAB"))   # Powinno zwrócić "brak"
