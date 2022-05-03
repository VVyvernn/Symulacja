def FCFS(processes):
    n = len(processes)
    # wszystkie procesy mają wartości: arrival, burst, work i name
    # work to zmienna pomocnicza równa burst
    active_processes = []
    time = 0
    count = 0
    avg_tat = 0
    avg_wt = 0
    while True:
        # sprawdzamy czy przyszedł jakiś proces
        for i in range(n):
            if processes[i]["arrival"] == time:
                active_processes.append(processes[i])
        # jeśli jest jakiś aktywny i nie jest skończony zmniejszamy jego prace o 1
        for prcs in active_processes:
            if prcs["work"] != 0:
                prcs["work"] -= 1
                break
            # jeśli jakiś proces się skończł obliczamy dla niego WT i TAT i usuwamy z listy
            if prcs["work"] == 0:
                prcs["TAT"] = time - prcs["arrival"]
                prcs["WT"] = prcs["TAT"] - prcs["burst"]

                active_processes.pop(0)
                del prcs["work"]
                count += 1
        # pętla przerywa się gdy usuniemy wszystkie procesy czy kiedy wszystkie się skończą
        if count == n:
            break
        time += 1
    # obliczanie średnich czasów
    for i in processes:
        avg_wt += i["WT"]
        avg_tat += i["TAT"]
    avg_wt = avg_wt / n
    avg_tat = avg_tat / n
    results = [str(avg_tat), str(avg_wt)]
    for i in range(len(processes)):
        print(processes[i])

    return results

