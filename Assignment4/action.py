from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            if int(splittedline[1])!=0:
                list = repo.products.find(id=splittedline[0])
                if list[0].quantity>=-int(splittedline[1]):
                    newQ=list[0].quantity+int(splittedline[1])
                    repo.products.updateProduct(quantity=newQ,id=splittedline[0])
                    repo.activities.insert(Activitie(splittedline[0], splittedline[1], splittedline[2],splittedline[3]))

if __name__ == '__main__':
    main(sys.argv)