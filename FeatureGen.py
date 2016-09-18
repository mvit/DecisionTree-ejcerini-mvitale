import sys

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
        
        for label in labels:
            outfile.write(label)
            if (labels.index(label) < (len(labels)-1)):
                outfile.write(',')
        
        outfile.write('\n')
        
        for line in file:
            outfile.write(line.strip())
            #Piece in the lower left corner
            outfile.write('0,')
            #Pieces in the center
            outfile.write('0,')
            outfile.write('0,')
            #3 in a row pieces
            outfile.write('0,')
            outfile.write('0,')
            
        outfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])