

class Library(object):
    def __init__(self, index, books, signTime, rate, totScore, totDay):
        self.index = index
        self.books = books
        self.count = len(self.books) 
        self.signTime = signTime
        self.rate = rate
        self.totScore = totScore
        self.selectionScore = totScore * rate * (1 - signTime / totDay)
    
    def __repr__(self):
        return '[id:{}-len:{}-{}]'.format(self.index, self.count, self.books)

class Book(object):
    def __init__(self, index, score):
        self.index = index
        self.score = score
    
    def __repr__(self):
        return (repr(self.index, self.score))

class Scanner(object):
    def __init__(self, libIndex, bookIndex):
        self.libIndex = libIndex 
        self.bookIndex = bookIndex
        #self.score = score
    
    def __repr__(self):
        return '%s %s'%(self.libIndex, self.bookIndex)
