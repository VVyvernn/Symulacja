from FIFO import FIFO
from LRU import LRU
from FCFS import FCFS
from LCFS import LCFS
from generator import *
# seed generatora liczb-pseudo losowych aby oba algorytmy dostawały te same liczby
random.seed(1230)
# zapisywanie do pliku wyników obliczeń
file = open("test.txt", "w").close()
file = open("test.txt", "a")
ipt = int(input("pages or processes? 1/0 "))
if ipt == 1:
    n = int(input("How many pages: "))
    m = int(input("Size of frame: "))
    k = int(input("How many runs of the simulator: "))
    for i in range(k):
        file.write(FIFO(generator_pages(n), m))
        file.write("\n")
    file.write("\n")
    for i in range(k):
        file.write(LRU(generator_pages(n), m))
        file.write("\n")


elif ipt == 0:
    n = int(input("How many processes: "))
    k = int(input("How many runs of the simulator: "))
    min = int(input("Lowest value: "))
    max = int(input("Highest value: "))
    val = 1
    for i in range(k):
        testlist = FCFS(generator4(n, min, max))
        for x in testlist:
            file.write(x + " ")
            if val % 2 == 0:
                file.write("\n")
            val += 1
    file.write("\n")
    val = 1
    for i in range(k):
        testlist = LCFS(generator4(n, min, max))
        for x in testlist:
            file.write(x + " ")
            if val % 2 == 0:
                file.write("\n")
            val += 1

file.close()
