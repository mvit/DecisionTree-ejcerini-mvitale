import sys, math

class Node:
    feature = ""
    nodes = {}
    lines = []

def makeTree(outcomes, features):
    TotalEntropy = infoGain(outcomes, outcomes, True)

    gains = {}

    for feature in features:
        gains[feature] = TotalEntropy - infoGain(outcomes, features[feature], False)

    largest = 0

    n = Node()
    index = 0

    for feature in features:
        if(gains[feature[0]] > largest):
            largest = gains[feature[0]]
            n.feature = feature[0]
            features.index(feature)

    lineNums = {}

    for feature in features[index]:
        lineNums[feature] = []

    for feature in features[index]:
        lineNums[feature].append(featurelist[index].index(feature))

def infoGain(outcomes, features, total):

    TotalGain = 0

    countlist = {}
    gains = []
    
    for feature in features:
        countlist[feature] = [0,0,0]
    
    print(countlist)
    
    for idx in range(len(outcomes)):
        outcome = outcomes[idx]
        feature = features[idx]
        
        print((outcome, feature))
        if outcome=='1':
            countlist[feature][0] += 1
        elif outcome=='2':
            countlist[feature][1] += 1
        else:
            countlist[feature][2] += 1
    
    print(countlist)
    
    for val in countlist:
        count = countlist[val]
        print(count)
        total = count[0] + count[1] + count[2]
        totalRatio = total/float(len(outcomes))
        value = 0

        for c in count:
            if (c==0):
                value = 0
            else:
                countRatio = c/float(total)
                value -= countRatio * math.log(countRatio,2)

            print(value)

        if not total:
            value *= totalRatio

        gains.append(value)

    for value in gains:
        TotalGain += value

    return TotalGain

def main(argv):
    if (len(argv) < 2):
        print("USAGE: python DecisionTree.py infile.csv num_folds")
        return 0
    
    with open(argv[0], 'r') as file:
        #Do feature recognition
        labels = file.readline().strip().split(',')
        feat_idx = labels.index('winner')
        featurenames = labels[feat_idx + 1:]
        print(featurenames)
        
        outcomes = []
        features = {}
        
        #Add arrays per feature
        for name in featurenames:
            features[name] = []

        #Do feature reading
        for line in file:
            board = line.strip().split(',')
            outcomes.append(board[feat_idx])

            for name in featurenames:
                name_idx = featurenames.index(name)
                features[name].append(board[feat_idx + 1 + name_idx])

        #Build the tree by information gain
        for feature in features:
            print(feature)
            infoGain(outcomes, features[feature], False)

if __name__ == "__main__":
    main(sys.argv[1:])

