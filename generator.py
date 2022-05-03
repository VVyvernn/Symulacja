import random, numpy
# wszystkie generatory użyte w programie

def generator1(n):
    processes = []

    for i in range(n):
        a = int(
            numpy.random.default_rng(10).choice(numpy.random.normal(50, 10, int(n) * 2 + 10), replace=False).round())
        b = int(
            numpy.random.default_rng(10).choice(numpy.random.normal(50, 10, int(n) * 2 + 10), replace=False).round())
        processes.append(
            {"name": f"P{i + 1}",
             "arrival": a,
             "work": b,
             "burst": b})
    return processes


def generator2(n):
    processes = []
    min = int(input("Lowest value: "))
    max = int(input("Highest value: "))

    for i in range(n):
        a = int(random.randrange(min, max))
        b = int(random.randrange(min, max))
        processes.append(
            {"name": f"P{i + 1}",
             "arrival": a,
             "work": b,
             "burst": b})
    return processes


def generator3(n, min, max):
    processes = []
    for i in range(n):
        a = 0
        b = int(random.randrange(min, max))
        processes.append(
            {"name": f"P{i + 1}",
             "arrival": a,
             "work": b,
             "burst": b})
    return processes


def generator_pages(n):
    pages = []
    for i in range(n):
        b = int(random.randrange(1, 50))
        pages.append(b)
    return pages


def generator4(n, min, max):
    processes = []
    for i in range(n):
        a = int(random.randrange(min - 1, max))
        b = int(random.randrange(min, max))
        processes.append(
            {"name": f"P{i + 1}",
             "arrival": a,
             "work": b,
             "burst": b})
    return processes
