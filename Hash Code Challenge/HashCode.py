
num_libs = 0
all_books = []

class Library:
    def __init__(self, books, days_to_screen, books_per_day):
        self.books = books
        self.days_to_screen = days_to_screen
        self.books_per_day = books_per_day

    def get_output(self):
        return min()

    def rembook(self, id):
        self.books.remove(id)


# reading file
with open('a_example.txt', 'r') as f:
    input = f.read()


lines = input.split('\n')

totalBooks = lines[0][0]
totalLibraries = lines[0][1]
totalDays = lines[0][2]

answer = ''

libraryScore = computeLibraryScore(library, daysAvailable)


#writing the output file
o = open('output.txt', 'w')

o.write(answer)
f.close()
o.close()

