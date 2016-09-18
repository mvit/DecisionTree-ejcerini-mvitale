import sys, math

def infogain(outcome, feature):
    
def main(argv):
    if (len(argv) < 2):
        print("USAGE: python DecisionTree.py infile.csv num_folds")
    
    with open(argv[0], 'r') as file:
        #Do feature recognition
        labels = file.readline().strip().split(',')
        feat_idx = labels.index('winner')
        features = labels[feat_idx + 1:]
        print(features)
        
        #Do feature reading
        for line in file:
            
        #Build the tree by information gain
        for feature in features:
            
if __name__ == "__main__":
    main(sys.argv[1:])