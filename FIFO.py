def FIFO(pages, size_of_frame):
    # licznik sprawdza na który następny indeks będzie zastąpiony
    # jesli osiągnie rozmiar ramki jest zerowany
    number = 0
    # ramka
    frame = []
    faults = 0
    for i in pages:
        if number >= size_of_frame:
            number = 0
            # jeśli ramka nie jest pusta sprawdzamy czy ramka ma miejsce
            # i czy nasza strona jest w ramce, jesli nie dodajemy ją i dodajemy chybienie
        if len(frame) < size_of_frame:
            if i not in frame:
                frame.append(i)
                faults += 1
            # sprawdzamy czy strona jest w ramce jesli nie to dodajemy ja
            # dodajemy chybienie i zwiekszamy "licznik"
        else:
            if i not in frame:
                frame[number] = i
                number += 1
                faults += 1

    return str(faults)
