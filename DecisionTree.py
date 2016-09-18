import sys, math

def infoGain(outcomes, features):
    TotalGain = 0;

    countlist = {}
    for features in feature:
        countlist[feature] = [0,0,0]

    for outcome in outcomes:
        idx = outcomes.index(outcome)
        feature = features[idx]
        if outcome.equals('1'):
            countlist[feature][0] += 1
        elif outcome.equals('2'):
            countlist[feature][1] += 1
        else:
            countlist[feature][2] += 2


def main(argv):
    if (len(argv) < 2):
        print("USAGE: python DecisionTree.py infile.csv num_folds")
    
    with open(argv[0], 'r') as file:
        #Do feature recognition
        labels = file.readline().strip().split(',')
        feat_idx = labels.index('winner')
        featurenames = labels[feat_idx + 1:]
        print(features)
        
        outcomes = []
        features = {}
        
        #Add arrays per feature
        for name in featurenames:
            features[name] = []

        #Do feature reading
        for line in file:
            board = line.strip().split(',')
            print(board)
            outcomes.append(board[feat_idx])

            for name in featurenames:
                name_idx = featurenames.index(name)
                features[name].append(board[feat_idx + name_idx])

        #Build the tree by information gain
        for feature in features:
            
if __name__ == "__main__":
    main(sys.argv[1:])


