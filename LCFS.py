def LCFS(processes):

    active_processes = []
    # lsita na element który jest wykonywany
    working_processes = []
    time = 0
    count = 0
    avg_wt = 0
    avg_tat = 0
    n = len(processes)
    while True:
        # sprawdzamy czy przyszedł jakiś proces jeśli tak to dajemy go albo do
        # pracujących procesów jeśli ta lista jest pusta jeśli nie dajemy
        # do aktywnych
        for i in range(n):
            if processes[i]["arrival"] == time:
                if len(working_processes) == 0:
                    working_processes.append(processes[i])
                else:
                    active_processes.append(processes[i])
        # ten sam mechanizm co w FCFS tylko, że na pracującym procesie
        for prcs in working_processes:
            if prcs["work"] != 0:
                prcs["work"] -= 1

            if prcs["work"] == 0:
                prcs["TAT"] = time - prcs["arrival"]
                prcs["WT"] = prcs["TAT"] - prcs["burst"]
                working_processes.pop(0)
                count += 1
                # upewniamy się że usuwamy dobry proces i sprwadzamy wszystkie możliwości
                if len(active_processes) == 0:
                    pass
                elif len(active_processes) != 1:
                    working_processes.append(active_processes[-1])
                else:
                    working_processes.append(active_processes[0])
                num = 0
                for y in active_processes:
                    if y["name"] == working_processes[0]["name"]:
                        active_processes.pop(num)
                    num += 1
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
    return results
