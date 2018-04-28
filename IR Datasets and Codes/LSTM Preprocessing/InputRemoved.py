import numpy as np
 

def ConvertInputNumberToBinary(n, N):
	if(n > N): 
		return np.zeros(N)
	temp = np.zeros(N)
	temp[n-1] = 1
	return list(temp)


filename = "/Users/karthikeyan/Desktop/IR Project/TestingData.txt"
f = open(filename, "r") 
data = f.read().split("\n")
data.pop()

Input 	= []
Output 	= []
Target	= []


for i in range(0, len(data)):
	try:
		data[i] = data[i].split("\t")
		temp = list(filter(None, data[i][0].split(" ") ))
		Input.append(temp)
		temp = list(filter(None, data[i][1].split(" ") ))
		Output.append(temp)
		Target.append(Output[i][1:])
	except:
		print("Two inputs not available")



countError = 0
for i in range(len(Input)):
	for j in range(len(Input[i])):
		try:
			Input[i][j] = ConvertInputNumberToBinary(int(Input[i][j]) ,  int(28) )
		except:
			print(Input[i][j])
			countError = countError + 1



countError = 0
for i in range(len(Output)):
	for j in range(len(Output[i])):
		try:
			Output[i][j] = ConvertInputNumberToBinary(int(Output[i][j]) ,  int(315) )
		except:
			print("Output Error :" , Output[i][j]) 
			countError = countError + 1
	Output[i] = [ConvertInputNumberToBinary(1, 315)] + Output[i]
	Output[i].append(ConvertInputNumberToBinary(int(315) ,  int(315) ))



Target	= []

for i in range(len(Output)):
	Target.append(Output[i][1:])



















