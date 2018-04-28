import sys
import pickle

from googletrans import Translator;
translator = Translator()

name = sys.argv[1]

with open(name, 'rb') as f:
	f = pickle.load(f)



for i in range(0, len(f)):
    try:
        a = translator.translate(f[i], dest='hi')
        print(i, "\t", f[i] ,"\t", a.text);
    except:
        print("error has occured")


