import sys

def main(argv):
    if (len(argv) < 1):
        print("python DecisionTree.py infile.csv")
    
    with open(argv[0], 'r') as file:
        #Do feature recognition
        labels = file.readline().strip().split(',')
        feat_idx = labels.index('winner')
        features = labels[feat_idx + 1:]
        print(features)
        
        
if __name__ == "__main__":
    main(sys.argv[1:])