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


