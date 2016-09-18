import sys

def bottomleft(line):
    return line[0]

def center(line):
    center = []
    for idx in range(1, 6):
        center.append(line[3*idx:5*idx])
    p1 = center.count('1')
    p2 = center.count('2')
    if (p1 > p2):
        return 1
    else:
        return 2
    return 0

def threeinrow(line):
    count = 0
    p1threes = 0
    p2threes = 0



    return 0

def btmcenter(line):
    bottom = line[3:5]
    p1 = bottom.count('1')
    p2 = bottom.count('2')
    
    if (p1 > p2):
        return 1
    else:
        return 2
    return 0

def btmcount(line):
    bottom = line[0:7]
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
            outfile.write(line.strip())
            board = line.split(',')
            #Piece in the lower left corner
            outfile.write(bottomleft(board) + ',')
            #Pieces in the center
            outfile.write('%d ,' % center(board))
            #3 in a row pieces
            outfile.write('%d ,' % threeinrow(board))
            #Bottom Count
            outfile.write('%d ,' % btmcount(board))
            #Bottom Center
            outfile.write('%d ,' % btmcenter(board))
            
            outfile.write('\n')
        outfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])