def get_input(file):
    with open(file, 'r') as f:
        input = f.read()

    lines = input.split('\n')

    values = lines[0].split(' ')
    num_books = int(values[0])
    num_libs = int(values[1])
    D = int(values[2])

    values = lines[1].split(' ')
    S = []
    for i in range(num_books):
        S.append(int(values[i]))

    T = []
    M = []
    L = []
    libraries = []
    for i in range(num_libs):
        values = lines[2*i + 2].split(' ')
        lbooks = []
        lnumb = int(values[0])
        dts = int(values[1])
        bpd = int(values[2])
        values = lines[2*i + 3].split(' ')
        for j in range(lnumb):
            b = int(values[j])
            score = S[b]
            notfound = True
            for k in range(len(lbooks)):
                if score >= S[lbooks[k]]:
                    lbooks.insert(k, b)
                    notfound = False
                    break
            if notfound:
                lbooks.append(b)
        L.append(lbooks)
        T.append(dts)
        M.append(bpd)
    return (S, T, M, L, D)
	
def potential(lib, day, S, T, M, L, D, availBooks):
    firstDay = day + T[lib]
    if firstDay >= D:
        return 0
    availDays = D - firstDay
    potent = 0
    books = []
    for bookId in L[lib]:
        if len(books) == availDays * M[lib]:
            break
        if not availBooks[bookId]:
            continue
        books.append(bookId)
        potent += S[bookId]
    return (potent, books)
	
def run(file):
    S, T, M, L, D = get_input(file)
    availBooks = [True] * len(S)
    availLibs = [True] * len(L)
    currDay = 0
    score = 0
    libs = []
    while True:
        maxLib = -1
        maxPotent = (0, [])
        for i in range(len(L)):
            if not availLibs[i]:
                continue
            potenti = potential(i, currDay, S, T, M, L, D, availBooks)
            if potenti[0] > maxPotent[0]:
                maxPotent = potenti
                maxLib = i
        if maxLib == -1:
            break
        availLibs[maxLib] = False
        score += maxPotent[0]
        for book in maxPotent[1]:
            availBooks[book] = False
        libs.append((maxLib, maxPotent[1]))
    outstr = ""
    outstr += str(len(libs)) + "\n"
    for lib in libs:
        outstr += str(lib[0]) + " " + str(len(lib[1])) + "\n"
        s = ""
        for book in lib[1]:
            s += str(book) + " "
        outstr += s + "\n"
    print("Final Score: " + str(score))
    with open(file + ".out", 'w') as f:
        f.write(outstr)