from tqdm import tqdm
import operator
from operator import attrgetter
from library import *


def bestLib(libDesc, dayLeft, scores):

    bestScore = 0
    bestlib = []

    i = 0
    index = 0

    # print(libDesc)
    for i, lib in (enumerate((libDesc))):
        # temp = lib.totScore * lib.rate * (1 - lib.signTime / dayLeft)
        tempDayLeft = dayLeft - lib.signTime
        maxBooksScanned = tempDayLeft * lib.rate
        maxPossibleScore = 0

        it = 0
        while(it < maxBooksScanned and it < lib.count):
            if int(scores[int(lib.books[it])]) != -1:
                maxPossibleScore += int(scores[int(lib.books[it])])
            else:
                maxBooksScanned += 1
            it += 1
        # print(maxPossibleScore,i)
        temp = maxPossibleScore / lib.signTime
        if(temp > bestScore):
            bestScore = temp
            bestlib = lib
            index = i

    return (bestlib, index)


def readF(filename):
    f = open(filename)

    nBooks, nLib, totDay = [int(x) for x in f.readline().split(' ')[0:3]]

    scores = []

    libDesc = []
    scores = f.readline().replace('\n', '').split(' ')
    scores = [int(x) for x in scores]

    for i in range(nLib):
        _, signTime, rate = [int(x) for x in f.readline().split(' ')[0:3]]
        books = f.readline().replace('\n', '').split(' ')
        books = [int(x) for x in books]
        totScore = 0
        for book in books:
            totScore += int(scores[int(book)])

        books.sort(key=lambda x: int(scores[int(x)]), reverse=True)

        libDesc.append(
            Library(i, books, signTime, rate, totScore, totDay)
        )

    return nBooks, nLib, totDay, scores, libDesc


def outF(filename, final, scores):
    score = 0
    f = open(filename, 'w+')

    f.write(str(len(final)) + '\n')

    for lib in final:
        f.write('{}\n'.format(lib[0].libIndex))
        s = ''
        #s = ' '.join( [str(p.bookIndex) for p in lib ] )
        for p in lib:
            s = s + (str(p.bookIndex) + ' ')
            score += int(scores[int(p.bookIndex)])
        f.write('{}\n'.format(s))
    print(score)
    f.close()


def solveAll(filename):
    nBooks, nLib, totDay, scores, libDesc = readF(filename)
    dayLeft = totDay
    scores_mod = scores.copy()

    scanned = [0] * (nBooks + 1)

    final = []
    hello = 0

    tempLibDesc = libDesc.copy()

    while(dayLeft > 0):
        print(dayLeft)
        library, index = bestLib(tempLibDesc, dayLeft, scores_mod)

        if(not library):
            break

        libArray = []
        dayLeft -= library.signTime

        maxPossibleScans = dayLeft * library.rate
        count = library.count


        it = 0
        while(it < count and it < maxPossibleScans):

            if scanned[library.books[it]] == 1:
                it += 1
                maxPossibleScans += 1

            else:
                hello += 1
                temp = Scanner(library.index, int(library.books[it]))
                scores_mod[library.books[it]] = -1
                scanned[int(library.books[it])] = 1
                libArray.append(temp)
                it += 1
        if(len(libArray) != 0):
            final.append(libArray)

        # print(library.index)
        tempLibDesc.pop(index)


    # print(scanned)
    print(hello)
    outF(filename.replace('.txt', '') + '.out', final, scores)


#solveAll("a_example.txt")
#solveAll("b_read_on.txt")
#solveAll("c_incunabula.txt")
solveAll("d_tough_choices.txt")
#solveAll("e_so_many_books.txt")
#solveAll("f_libraries_of_the_world.txt")
