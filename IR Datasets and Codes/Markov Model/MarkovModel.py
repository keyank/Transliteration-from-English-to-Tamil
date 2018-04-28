from collections import Counter
import numpy as np

# Markov Model Error correcting algorithm

UniqueFullWord = {}
UniqueLtRt = {}



def GetReplacementCandidate( num ) :	
	# Return possible replacement candidates of num
	# Ans List or Array
	return []   



def GetSplitedList(word, k):
	EmptyList = []
	k = int(k)
	for i in range(k, len(word) - k):
		EmptyList.append(word[i-k:i+k+1])
	return EmptyList


	#	GetSplitedList('@@kkarthi@@' , 2)
	# 	Make each words in 2k +1 letter sequences each
	# 	e.g. word = karthikeyan, k = 2 , [karth , arthi, rthik, thike, hikey, ikeya, keyan]
def CreateMarkovSequence(Inputlst ,  k ):
	NewList = []
	for i in  range(0, len(Inputlst)):
		NewList =  GetSplitedList(Inputlst[i], k) +   NewList 
	return  NewList;



	#temp = CreateMarkovSequence(data, 1)
	# Take output of CreateMarkovSequence and return uique sequences with counts

def MakeUniqSequence(input  ):
	UniqDict = {}
	UniqDict = Counter( input )
	return UniqDict




def UniqLeftRight(inp , k):
	inp = np.asarray(inp)
	inp = list(np.delete(inp, k, axis=1))
	TempList = []
	for i in range(len(inp)):
		TempList.append('-'.join(inp[i]))
	return MakeUniqSequence(TempList)
	# Same as abpve function but before processing remove middle element




def GetProb( left, mid , right   ):
	FullStr = str(left) + "-" + str(mid) +  "-" + str(right)
	lfrt = str(left) + "-" + str(right)
	val1 = UniqueFullWord[FullStr]
	val2 = UniqueLtRt[lfrt]
	return val1/val2
	# given the left and right string return the probability of middle charecter
	# Easy to calculate return MakeUniqSequence - Output[left , mid, right]/UniqLeftRight-Output(left, right)




####################################################################################################################

	# 	Read unlabeled data
	# 	Create Markov sequence List
	#	Create Unique sequences
	# 	Create Uniq left rights
	#	Given a string to correct errors, ask for replacement candidates one by one if replcement gives more score then true (> 1.5 times)
	#		Then replace original with replaced.




filename = "/Users/karthikeyan/Desktop/IR Project/Markov Model/TrainData.txt"
f = open(filename, "r") 
data = f.read().split("\n")


for i in range(0, len(data)):
	data[i] = list('0') + list(filter(None, data[i].split(" ") )) + list('0')


k = 1;
MarList = CreateMarkovSequence(data , k)
StrMarList = []


for i in range(len(MarList)):
	StrMarList.append('-'.join(MarList[i]))



UniqueFullWord =MakeUniqSequence(StrMarList)
UniqueLtRt = UniqLeftRight(MarList, k)



import os
import pickle
os.chdir("/Users/karthikeyan/Desktop/IR Project/Markov Model/Model Parameters")

with open("UniqueFullWord.p", "wb") as fp:
	pickle.dump(UniqueFullWord, fp)



with open("UniqueLtRt.p", "wb") as fp:
	pickle.dump(UniqueLtRt, fp)



#GetProb("198", "293", "153")

# 198-293-153
# 115-198-207
















