from tqdm import tqdm
import operator
from operator import attrgetter
from library import *

def readF(filename):
    f = open(filename)

    nBooks, nLib, totDay = [int(x) for x in f.readline().split(' ')[0:3]]

    scores = []
    libDesc = []

    scores = f.readline().replace('\n','').split(' ')

    for i in range(nLib):
        _, signTime, rate = [int(x) for x in f.readline().split(' ')[0:3]]
        books = f.readline().replace('\n','').split(' ')
        totScore = 0
        for book in books:
            totScore += int(scores[int(book)])

        books.sort(key = lambda x: int(scores[int(x)]), reverse = True)

        libDesc.append(
            Library(i, books, signTime, rate, totScore, totDay)
        )
        #print(libDesc[i].selectionScore)
    
    # libDesc.sort(key = attrgetter('selectionScore'), reverse = True)   
    libDesc.sort(key = lambda x: x.selectionScore, reverse = True)        
    
    return nBooks, nLib, totDay, scores, libDesc
readF("a_example.txt")

def outF(filename, final, scores):
    score = 0
    f = open(filename, 'w+')

    f.write(str( len(final) ) + '\n')

    for lib in final:
        f.write('{}\n'.format(lib[0].libIndex))
        s = ''
        #s = ' '.join( [str(p.bookIndex) for p in lib ] )
        for p in lib:
            s = s + (str(p.bookIndex) + ' ')
            score += int(scores[int(p.bookIndex)])
        f.write( '{}\n'.format(s) )
    print(score)
    f.close()

def solveAll(filename): 
    nBooks, nLib, totDay, scores, libDesc = readF(filename)
    dayLeft = totDay
    
    scanned = []
    final = []
    hello = 0
    for library in tqdm(libDesc):
        libArray = []
        dayLeft -= library.signTime
        
        maxPossibleScans = dayLeft * library.rate
        count = library.count
        
        # if(library.count < maxPossibleScans):
        #     maxPossibleScans = library.count
        # for i in range maxPossibleScans:

        it = 0
        while(it < count and it < maxPossibleScans):
            
            if(any(x.bookIndex == library.books[it] for x in scanned)):
                it += 1

            else:    
                hello += 1
                temp = Scanner(library.index, int(library.books[it]))
                scanned.append(temp)
                libArray.append(temp)
                it += 1
        if(len(libArray) != 0):
            final.append(libArray)

    scanned.sort(key = lambda x: x.libIndex)
    #print(scanned)
    print(hello)

    outF( filename.replace('.txt', '') +'.out', final, scores)


# solveAll("a_example.txt")
# solveAll("b_read_on.txt")
# solveAll("c_incunabula.txt")
# solveAll("d_tough_choices.txt")
solveAll("e_so_many_books.txt")
solveAll("f_libraries_of_the_world.txt")





