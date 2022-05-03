def LCFS3(processes):
    active = {"burst": -1, "work": -1}
    active_id = 0
    n = len(processes)
    active_processes = []
    time = 0
    count = 0
    avg_tat = 0
    avg_wt = 0
    while count != n:
        for i in range(n):
            if processes[i]["arrival"] == time:
                active_processes.append(processes[i])

        if len(active_processes) > 0:
            if active["work"] > 0:
                active["work"] -= 1

            if active["work"] == 0:
                active["TAT"] = time - active["arrival"]
                active["WT"] = active["TAT"] - active["burst"]
                active_processes.pop(active_id)
                count += 1
                active["work"] = -1

        if active["work"] == -1:
            if len(active_processes):
                active = active_processes[-1]
                active_id = len(active_processes) - 1
        time += 1
    for i in processes:
        avg_wt += i["WT"]
        avg_tat += i["TAT"]
    avg_wt = avg_wt / n
    avg_tat = avg_tat / n
    results = [str(avg_tat), str(avg_wt)]
    return results
