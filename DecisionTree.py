import sys, math, array, copy

class Node:

    def __init__(self):
        self.feature = ""
        self.nodes = {}

    def addNode(self, label, node):
        print("Adding node")
        self.nodes[label] = node
    
    def setFeature(self, label):
        self.feature = label

    def printNode(self):
        print("Node Feature")
        print(self.feature)
        print("Splits")
        print(self.nodes)
        count = 0
        for node in self.nodes:
            count+=1
            print(count)
            print(self.nodes[node].feature)
        for node in self.nodes:
            if self.nodes[node]:
                self.nodes[node].printNode()

def makeTree(node, outcomes, features):
    if not features:
        print("End of Tree")
        return None

    print("Tree on")
    print(node)
    TotalEntropy = infoGain(outcomes, outcomes, True)

    gains = {}
    
    maxval = 0
    best = ''
    for feature in features:
        info = infoGain(outcomes, features[feature], False)
        val = float(TotalEntropy) - infoGain(outcomes, features[feature], False)
        
        if (val < maxval):
            maxval = val
            best = feature

    node.setFeature(best)

    for value in set(features[best]):
        print(value)
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
        print("adding child for node {0}".format(best))
        child = makeTree(Node(), new_outcomes, new_features)
        if child :
            print("child {0} valid".format(value))
            node.addNode(value, child)
        else:
            print("child is empty")
            break

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

def k_fold_data(data, k):
    dset = []
    random.shuffle(data)
    fold_size = len(data)//k
    for i in range(fold_size):
        dset.append((data[i:i*k]))
    return dset

def printTree(node):
    tree = bfs(node)

    for n in tree:
        if n == "NEXT":
            sys.stdout.write("\n")
        else:
            sys.stdout.write(n + " ")

def bfs(node):
    visited = []
    queue = []
    tempqueue = []

    outofchildren = False

    visited.add(node.feature)
    visited.add("NEXT")

    for n in node.nodes:
        queue.add(n)

    while not outofchildren:

        while queue:

            n = queue.pop(0)

            visited.add(n.feature)

            for child in n.nodes:
                tempqueue.add(child)

        visited.add("NEXT")

        if tempqueue:
            queue = tempqueue
        else:
            outofchildren = True

    return visited

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

        kfolds = k_fold_data
        #Build the tree by information gain
        tree = makeTree(Node(), outcomes, features)
        print('THIS IS DAD')
        printTree(tree)


if __name__ == "__main__":
    main(sys.argv[1:])

