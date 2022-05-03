def LRU(pages, size_of_frame):
    frame = []
    faults = 0
# przechodzimy przez wszystkie strony
    for i in pages:
        # sprawdzamy czy ramka jest mniejsza od swojej maksymalnej pojemnosci
        # jesli nie to dodajemy strone
        if len(frame) < size_of_frame:
            frame.append(i)
            faults += 1
        else:
            # jesli jest pelna sprawdzamy którą stronę usunąć
            # strona o indeksie 0 zawsze jest tą która jest najdłużej w programie
            # a o indeksie len(ramka) - 1 to ta która jest najkrócej
            if i in frame:
                for x in range(len(frame)):
                    if i == frame[x]:
                        frame.insert(len(frame) - 1, frame.pop(x))
            # usuwamy najstarszą stronę
            else:
                frame.append(i)
                del frame[0]
                faults += 1

    return str(faults)
