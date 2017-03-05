#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import listdir
import numpy
from numpy import *
import operator

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    #print diffMat
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    #print len(sqDistances)
    #exit()
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()

    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2Data(filename):
	 file_handle = open(filename)
	 vector = zeros(1024)
	 for i in range(32):
	 	line = file_handle.readline()
	 	for j in range(32):
	 		vector[i*32+j] = int(line[j])
	 return vector

#print img2vector('0_0.txt')

def getDir(trainingDirName,testDirName):
	trainingFileNames = listdir(trainingDirName)
	trainingFileCount = len(trainingFileNames)
	trainingDataSet = zeros((trainingFileCount,1024))
	trainingResult = zeros((trainingFileCount))
	for i in range(trainingFileCount):
		trainingFileName = trainingFileNames[i]
		trainingDataSet[i] = file2Data(trainingDirName+'/'+trainingFileName)
		trainingResult[i] = int(trainingFileName.split('.')[0].split('_')[0]);

	testFileNames = listdir(testDirName)
	testFileCount = len(testFileNames)
	errorCount = 0
	for i in range(testFileCount):
		trueResult = int(testFileNames[i].split('.')[0].split('_')[0]);
		testData =  file2Data(testDirName+'/'+testFileNames[i])
		testResult = classify(testData,trainingDataSet,trainingResult,5)
		#print "the testResult  is %d ,the trueResult is %d"  %(testResult,trueResult)
		if  (testResult != trueResult):
			errorCount += 1
	print "the errorCount is %d" % (errorCount)
	print "the error of rate is %f" % (errorCount/float(testFileCount))
#getDir('./trainingDigits','/root/文档/machinelearninginaction/Ch02/testDigits')

