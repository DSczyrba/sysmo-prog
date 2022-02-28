import random



def markt_erzeugen(DIM_X, DIM_Y, REGALE):
    alle_reihen = []

    for _ in range(DIM_Y):
        eine_reihe = []
        for i in range(DIM_X):
            if random.randrange(0, 10) <= int(REGALE / 10):
                eine_reihe.append("x")
            else:
                eine_reihe.append("#")
        alle_reihen.append(eine_reihe)

    return "\n".join("".join(line) for line in alle_reihen)