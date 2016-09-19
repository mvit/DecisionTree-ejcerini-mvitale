import sys, math, array, copy

class Node:
    feature = ""
    nodes = {}
    
    def printNode(self):
        # print(self.feature)
        # for node in self.nodes:
        #     print("Child {0} of {1}".format(self.nodes.index(node),self.feature))
        #     if node:
        #         node.printNode()
        return self.feature

    def _init_(self):
        self.feature = ""
        self.nodes = []

def makeTree(node, outcomes, features):
    if not features:
        return None
    
    TotalEntropy = infoGain(outcomes, outcomes, True)

    gains = {}
    
    maxval = 0
    best = ''
    for feature in features:
        info = infoGain(outcomes, features[feature], False)
        val = float(TotalEntropy) - infoGain(outcomes, features[feature], False)
        print(info)
        print(val)
        
        if (val < maxval):
            maxval = val
            best = feature

    node.feature = best

    print(node.feature)

    for value in set(features[best]):
        node.nodes[value] = None
        
        #Get new example list
        notbest = copy.deepcopy(features)
        del notbest[best]
        #print(notbest)
        new_features = {}
        new_outcomes = []

        ids =  [i for i,x in enumerate(features[best]) if x == value]
        
        for feature in notbest:
            new_features[feature] = []

        for idx in ids:
            new_outcomes.append(outcomes[idx])
            for feature in notbest:
                new_features[feature].append(features[feature][idx])

        #Make a subtree from those
        node.nodes[value] = makeTree(Node(), new_outcomes, new_features)

    return node

def infoGain(outcomes, features, total):

    TotalGain = 0

    countlist = {}
    gains = array.array('f')
    
    for feature in features:
        countlist[feature] = [0,0,0]
    
    for idx in range(len(outcomes)):
        outcome = outcomes[idx]
        feature = features[idx]
        #print((outcome, feature))
        if outcome=='1':
            countlist[feature][0] += 1
        elif outcome=='2':
            countlist[feature][1] += 1
        else:
            countlist[feature][2] += 1

    for val in countlist:
        count = countlist[val]
        total = count[0] + count[1] + count[2]
        totalRatio = total/float(len(outcomes))
        value = 0

        for c in count:
            if (c==0):
                value = 0
            else:
                countRatio = c/float(total)
                value -= float(countRatio) * math.log(countRatio,2)
                
            if not total:
                value *= totalRatio
            gains.append(value)

    for value in gains:
        TotalGain += float(value)

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
        tree = makeTree(Node(), outcomes, features)
        tree.printNode()


if __name__ == "__main__":
    main(sys.argv[1:])

