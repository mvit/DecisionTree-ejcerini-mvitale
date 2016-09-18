import sys, math

def makeTree(outcomes, featurelist):
    TotalEntropy = infoGain(outcomes, outcomes, True)

    gains = {}

    for feature in featurelist:
        gains[feature[0]] = TotalEntropy - infoGain(outcomes, feature, False)


    largest = 0

    n = Node()
    index = 0

    for feature in featurelist:
        if(gains[feature[0]] > largest):
            largest = gains[feature[0]]
            n.feature = feature[0]
            featurelist.index(feature)


    lineNums = {}

    for feature in featurelist[index]:
        lineNums[feature] = []

    for feature in featurelist[index]:
        lineNums[feature].append(featurelist[index].index(feature))





def infoGain(outcomes, features, total):

    TotalGain = 0

    countlist = {}
    gains = []
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
            countlist[feature][2] += 1

    for count in countlist:
        total = count[0] + count[1] + count[2]
        totalRatio = total/len(outcomes)

        value = 0
        for c in count:
            countRatio = c/total
            value -= countRatio * log(countRatio, 2)

        if not total:
            value *= totalRatio

        gains.append(value)

    for value in gains:
        TotalGain += value

    return TotalGain

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

class Node:
    feature = ""
    nodes = {}
    lines = []



