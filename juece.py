
from math import *

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

def calShannon(dataSet):
	map_ = {}
	shannon = 0
	len_ = len(dataSet)
	for data in dataSet:
		if data[-1] not in map_.keys():
			map_[data[-1]] = 1
		else:
			map_[data[-1]] +=1
	for i in map_:
		shannon -= float(map_[i])/len_ * log(float(map_[i])/len_,2)
	return shannon
#print calShannon(createDataSet()[0])

def splitDataSet(dataSet,index,value):
	returnValuePositive = []
	returnValueNegative = []
	for data in dataSet:
		if data[index] == value:
			returnValuePositive.append(data)
		else:
			returnValueNegative.append(data)
	return returnValuePositive,returnValueNegative
#print splitDataSet(createDataSet()[0],0,1)[1]

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calShannon(dataSet)

    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature

        uniqueVals = set(featList)       #get a set of unique values

        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)[0]
            
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calShannon(subDataSet)
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]	#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: 	#stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]

    myTree = {bestFeatLabel:{}}
    #del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        #subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value)[0],labels)
    return myTree

def juece(jueceTree,testFeature,features):
	firstNodeName = jueceTree.keys()[0];
	firstNodeData = jueceTree[firstNodeName];
	featureIndex = features.index(firstNodeName);
	featureData = testFeature[featureIndex]

	for  data in firstNodeData:
		if data == featureData:
			if type(firstNodeData[data]).__name__ == 'dict':
				class_ = juece(firstNodeData[data],testFeature,features)
			else:
				class_ =  firstNodeData[data]
	return class_
tree = createTree(createDataSet()[0],['no surfacing','flippers'])
print juece(tree,[1,1],['no surfacing','flippers'])


