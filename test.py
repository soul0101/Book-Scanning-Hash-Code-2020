from library import *

scanned = []
scanned.append(Scanner(1, 3, 25))
scanned.append(Scanner(1, 5, 14))



print(any(x.bookIndex == 2 for x in scanned))
