
from numpy import *

def loadData(fileName):
	fileHandler = open(fileName,'r')
	lines = fileHandler.readlines()
	size = len(lines)
	data1 = [[0,0] for i in range(size)]
	data2 = [0] * size

	for k,line in enumerate(lines):
		line =  line.strip().split();
		data1[k][0] = line[0]
		data1[k][1] = line[1]
		data2[k] = line[2]
	return data1,data2

def sigmoid(x):
	return 1/(1+exp(-x))

test = array([[1,2,3]])
test2 = array([[5,6,7],[1,2,3]])
print test * test2
#print loadData('./testSet.txt')

