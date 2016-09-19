import sys, math, array, copy, random
from collections import Counter

class Node:
    def __init__(self):
        self.feature = ""
        self.nodes = {}

    def addNode(self, label, node):
        self.nodes[label] = node

    def getFeature(self):
        return self.feature

    def setFeature(self, label):
        self.feature = label

    def printNode(self):
        print("Node Feature")
        print(self.feature)

        for node in self.nodes:
            if self.nodes[node]:
                self.nodes[node].printNode()

    def printTree(self):
        tree = self.bfs()

        for n in tree:
            if n == "NEXT":
                sys.stdout.write("\n")
            else:
                sys.stdout.write(n + " ")
        sys.stdout.write("\n")

    def bfs(self):
        queue = []
        visited = []
        queue.append(self)
        while queue:
            n = queue.pop(0)
            visited.append(n.feature)
            if n.nodes:
                visited.append("NEXT")
                visited.extend(n.nodes.keys())
                visited.append("NEXT")

            for child in n.nodes:
                queue.append(n.nodes[child])
        return visited

    def traverseTree(self, testData):
        if not self.nodes:
            return self.feature

        n = self.nodes[testData[self.feature]]

        return traverseTree(n, testData);

def makeTree(node, outcomes, features, m):
    TotalEntropy = getTotalEntropy(outcomes)
    gains = {}
    maxval = 0.0
    best = ''

    if ((len(outcomes) == 1) or (not features) or (TotalEntropy == 0.0)):
        child = Node()
        child.setFeature(str(m))
        return child

    for feature in features:
        info = infoGain(outcomes, features[feature])
        val = float(TotalEntropy - info)
        if (best == ''):
            best = feature
        if (val > maxval):
            maxval = val
            best = feature

    node.setFeature(best)
    for value in set(features[best]):        #Get new example list

        notbest = copy.deepcopy(features)
        del notbest[best]

        new_features = {}
        new_outcomes = []

        ids =  [i for i,x in enumerate(features[best]) if x == value]
        
        for feature in notbest:
            new_features[feature] = []
        for idx in ids:
            new_outcomes.append(outcomes[idx])
            for feature in notbest:
                new_features[feature].append(features[feature][idx])

        mcount = Counter(new_outcomes)
        commonm = mcount.most_common(1)[0]
        newm = int(commonm[0])

        #Make a subtree from those
        child = makeTree(Node(), new_outcomes, new_features, newm)
        if child :
            node.addNode(value, child)

    return node

def getTotalEntropy(outcomes):

    count = {}
    value = 0
    total = len(outcomes)

    for out in outcomes:
        count[out] = 0

    for out in outcomes:
        count[out] += 1

    for c in count:
        countRatio = count[c]/float(total)
        value -= float(countRatio) * math.log(countRatio, 2)

    return value

def infoGain(outcomes, features):

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
                pass
            else:
                countRatio = c/float(total)
                value -= float(countRatio) * math.log(countRatio,2)

        value *= totalRatio
        gains.append(value)

    for value in gains:
        TotalGain += float(value)

    return TotalGain

def k_fold_data(data, k):
    dset = []
    random.shuffle(data)
    fold_size = len(data)//k
    for i in range(k):
        dset.append((data[0 + (i*fold_size): fold_size - 1 + (i*fold_size)]))
    return dset

def runTests(tree, testData):
    successes = 0
    failures = 0

    for test in testData:
        result = tree.traverseTree(test)
        if result is test[outcome]:
            successes += 1
        else:
            failures += 1

    print("{0} tests were run. There were {1} successes and {2} failures.".format(len(testData), successes, failures))
    error = failures/float(len(testData)) * 100
    print("The percent error of this training session is {0}%".format(error))
    return error

def main(argv):
    if (len(argv) < 2):
        print("USAGE: python DecisionTree.py infile.csv num_folds")
        return 0

    with open(argv[0], 'r') as file:
        #Do feature recognition
        labels = file.readline().strip().split(',')
        feat_idx = labels.index('winner')
        featurenames = labels[feat_idx + 1:]

        dataset = []
        learnset = []
        testset = []

        #Do feature reading
        for line in file:
            dataset.append(line)

        learnset = k_fold_data(dataset, int(argv[1]))
        outcomes = []
        features = {}

        #Add arrays per feature
        for name in featurenames:
            features[name] = []
        for sets in learnset:
            testset.append(sets[0])
            for data in sets[1:]:
                board = data.strip().split(',')
                outcomes.append(board[feat_idx])
                for name in featurenames:
                    name_idx = featurenames.index(name)
                    features[name].append(board[feat_idx + 1 + name_idx])

        #Build the tree by information gain
        tree = makeTree(Node(), outcomes, features, 0)
        tree.printTree()
        #Test data


if __name__ == "__main__":
    main(sys.argv[1:])

