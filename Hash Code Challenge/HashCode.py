import null as null


class Library:
    def __init__(self, b, dts, bpd):
        self.books = b
        self.days_to_screen = dts
        self.books_per_day = bpd

    def get_output(self):
        return min()

    def rembook(self, id):
        self.books.remove(id)


def get_input(file)
    with open(file, 'r') as f:
        input = f.read()

    lines = input.split('\n')

    values = lines[0].split(' ')
    num_books = values[0][0]
    num_libs = values[0][1]
    days = values[0][2]

    values = lines[1].split(' ')
    books = []
    for i in range(num_books):
        books.append((values[i], True))

    libraries = []
    for i in range(num_libs):
        values = lines[2*i + 2].split(' ')
        lbooks = []
        lnumb = values[0]
        dts = values[1]
        bpd = values[2]
        values = lines[2*i + 3].split(' ')
        for j in range(lnumb):
            b = values[j]
            score = books[b][0]
            notfound = True
            for k in range(len(lbooks)):
                if score >= books[lbooks[k]][0]:
                    lbooks.insert(k, b)
                    notfound = False
                    break
            if notfound:
                lbooks.append(b)
        libraries.append(Library(lbooks, dts, bpd))
    return (books, libraries, days)



totalBooks = lines[0][0]
totalLibraries = lines[0][1]
totalDays = lines[0][2]

answer = ''


#writing the output file
o = open('output.txt', 'w')

o.write(answer)
f.close()
o.close()

