import sys
import pickle

file = open("/Users/karthikeyan/Desktop/Names Data/Translated Files/TamForHind.txt", "r")
f = file.read()
f = f.split("\n")
n = int(sys.argv[1])
l1 = int(len(f)/n)


fileout = open("/Users/karthikeyan/Desktop/Names Data/Translate/Script.sh" , "w+")
name1 = "/Users/karthikeyan/Desktop/Names\ Data/Translate/MultiFiles/"


for i in range(0, n):
	name = "/Users/karthikeyan/Desktop/Names Data/Translate/MultiFiles/" + str(i) 
	s = int(i*l1) 
	e = int ((i+1)*l1)
	with open(name, 'wb') as p:
		pickle.dump(f[s :e], p)
	fileout.write("python tr1.py " + name1+ str(i) + " &\n")

fileout.close()
file.close()


