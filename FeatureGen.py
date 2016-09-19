import sys
def board(line):
    board = []
    for col in range(0,6):
        carray = []
        for row in range(0,7):
            carray.append(line[(col*7) + row])
        board.append(carray)
    return board

def bottomleft(line):
    return line[0]

def center(line):
    center = []
    for idx in range(1,5):
        center.append(line[2*idx:4*idx])
    p1 = center.count('1')
    p2 = center.count('2')

    if (p1 > p2):
        return 1
    else:
        return 2
    return 0

def threeinrow(line):
    count = [0, 0, 0, 0]
    p1threes = 0
    p2threes = 0

    barray = board(line)

    for i in range(0,6):
        for j in range (0,7):
            if barray is not '0':
                currentPlayer = barray[i][j]
                for x in range(0,3):
                    if j + x < 7 and barray[i][j+x] == currentPlayer:
                        count[0] += 1;

                    if i + x < 6 and barray[i + x][j] == currentPlayer:
                        count[1] += 1;

                    if i + x < 6 and j + x < 7 and barray[i+x][j+x] == currentPlayer:
                        count[2] += 1;

                    if i - x <= 0 and j + x < 7 and barray[i-x][j+x] == currentPlayer:
                        count[3] += 1;
                if currentPlayer is '1':
                    for c in count:
                        if c >= 3:
                            p1threes += 1
                elif currentPlayer is '2':
                    for c in count:
                        if c >= 3:
                            p2threes += 1

    print("BOARD END")

    if p1threes > p2threes:
        return 1

    if p2threes > p1threes:
        return 2

    return 0

def btmcenter(line):
    bottom = line[2:4]
    p1 = bottom.count('1')
    p2 = bottom.count('2')
    
    if (p1 > p2):
        return 1
    else:
        return 2
    return 0

def btmcount(line):
    bottom = line[0:6]
    p1 = bottom.count('1')
    p2 = bottom.count('2')
    if (p1 > p2):
        return 1
    else:
        return 2
    return 0

def main(argv):
    #Every 6 digits is a column
    if (len(argv) < 2):
        print("USAGE: python FeatureGen.py infile.csv outfile.csv")
        return 0

    with open(argv[0], 'r') as file:
        outfile = open(argv[1], 'w')
        #Parse labels
        labels = file.readline().strip().split(',')
        print(labels)
        labels.append('bottomleft')
        labels.append('center')
        labels.append('3inrow')
        labels.append('btmcount')
        labels.append('btmcenter')

        for label in labels:
            outfile.write(label)
            if (labels.index(label) < (len(labels)-1)):
                outfile.write(',')
        
        outfile.write('\n')
        
        for line in file:
            outfile.write(line.strip() + ',')
            board = line.split(',')
            #Piece in the lower left corner
            outfile.write(bottomleft(board) + ',')
            #Pieces in the center
            outfile.write('%d,' % center(board))
            #3 in a row pieces
            outfile.write('%d,' % threeinrow(board))
            #Bottom Count
            outfile.write('%d,' % btmcount(board))
            #Bottom Center
            outfile.write('%d' % btmcenter(board))
            
            outfile.write('\n')
        outfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])