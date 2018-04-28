from collections import Counter
import numpy as np
import os
import pickle



file = open("/Users/karthikeyan/Desktop/IR Project/Markov Model/ReplacementsNumbers.txt")
f = file.read()
f = f.split("\n")

ReplacementList = [[] for y in range(400) ]

for i in range(len(f)):
	f[i] = f[i].split("\t")
	try:
		x = int(f[i][0])
		y = int(f[i][1])
		ReplacementList[x].append(str(y))
	except:
		z = 0


k = 1
os.chdir("/Users/karthikeyan/Desktop/IR Project/Markov Model/Model Parameters")


with open("UniqueFullWord.p", "rb") as fp:
	UniqueFullWord = pickle.load(fp)



with open("UniqueLtRt.p", "rb") as fp:
	UniqueLtRt = pickle.load(fp)




def GetReplacementCandidate( number ) :
	num = int(number)
	return ReplacementList[num]



def GetProb( left, mid , right   ):
	FullStr = str(left) + "-" + str(mid) +  "-" + str(right)
	lfrt = str(left) + "-" + str(right)
	val1 = UniqueFullWord[FullStr]
	val2 = UniqueLtRt[lfrt]
	if (val2 == 0):
		return 0
	return val1/val2



def DecideReplace(middle, lst , left, right):
	trProb = GetProb(left, middle, right)
	max_prob = 0;
	max_candidate  = middle;
	for i in range(len(lst)):
		temp_prob  = GetProb(left, lst[i], right)
		if (temp_prob > max_prob):
			max_prob = temp_prob;
			max_candidate = lst[i]
	if(max_prob > 1*trProb):
		return max_candidate
	else:
		return -1


def Correct(input):
	k = 1
	for i in range(k, len(input) - k):
		relist = GetReplacementCandidate(input[i])
		lft = '-'.join(input[i-k:i])
		rgt = '-'.join(input[i+1: i+k+1])
		if(len(relist) > 0):
			val = DecideReplace(input[i]  , relist, lft, rgt)
			if(val != -1):
				input[i] = val
	return input





Input = "198 294 153"
Input = Input.split(" ")
Input = ['0']  + Input + ['0']

out = Correct(Input)
print(out)













