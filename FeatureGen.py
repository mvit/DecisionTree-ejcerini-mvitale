import sys

def main(argv):
    #Every 6 digits is a column
    if (len(argv) < 2):
        print("python FeatureGen.py infile.csv outfile.csv")
    
    with open(argv[0], 'r') as file:
        outfile = open(argv[1], 'w')
        #Parse labels
        labels = file.readline().strip().split(',')
        print(labels)
        labels.append('bottomleft')
        labels.append('p1center')
        labels.append('p2center')
        labels.append('p13inrow')
        labels.append('p23inrow')
        labels.append('p1btmcount')
        labels.append('p2btmcount')
        
        
        for label in labels:
            outfile.write(label)
            if (labels.index(label) < (len(labels)-1)):
                outfile.write(',')
        
        outfile.write('\n')
        
        for line in file:
            outfile.write(line.strip())
            #Piece in the lower left corner
            outfile.write('')
            #Pieces in the bottom
            outfile.write('')
        outfile.close()

if __name__ == "__main__":
    main(sys.argv[1:])