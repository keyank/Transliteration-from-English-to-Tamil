###################  Bidirectional Markov Model   #####################

Codes Folder : Markov Model

	MarkovModel.py
		Takes TrainData.txt as input and produces model parameters (probabilities/counts) as output.
		How to Run : python MarkovModelTest.py

	MarkovModelTest.py:
		Inputs:
			Take model parametres as input (output of MarkovModel.py).
			It takes the Tamil word to correct (in encoded numbers) as input (need to assign the the string to the  variable "Input" inside the code.)
			Takes ReplacementsNumbers.txt as input
		Output:
			Gives corrected word as output (stdout)
		How to run:
			python MarkovModelTest.py (better to use interactive python as the code is written for interactive checking)

	Folder : Markov Model Replacement Candidates:
		Codes to create replacement candidates






#####################  Translatation/Transliteration Data creation #############################


Codes Folder : Translate Codes
	CreateMultiFiles.py
		For paralilizing (otherwise very slow, by default creates 40 processes)
		Takes file to translate as input : need to change variable named "file" inside code.
	CombineAll.sh: 
		Translates the input in the "file" variable in CreateMultiFiles.py
		bash CombineAll.sh
	tr1.py
		Need to change target language inside code (change variable "a - dest ")






###########################  English To Hindi ###################################

Folder : English To Hindi
	
	Codes : English To Hindi/Data Creation Codes

	Eng2Hindi.txt		-	Data English-Name "TAB" Tamil-Name
	Eng2Hindi-Num.txt  	- 	Data Encoded English-Name "TAB" Encoded Tamil-Name, these are used as inputs
	Hindi2Num.sh		-	Encodes Hindi To Numbers   - Takes file to encode as inputs
	ConvertEng2Num.sh	- 	Encodes English to Numbers - Takse File to encode as input.

Similar for other language pairs also Tamil To Hindi, English To Tamil, Tamil To Hindi.






#####################  LSTM Sequence to Sequence Model ##########################
	
Folder : LSTM contains two Folder Eng2Tam Eng2Hin

	Folder : Eng2Tam

		Eng2Tam.py 			-	Contains the Transliterate code (English to tamil)
		InputData.txt		-	Contains the Input Data
		OutputData.txt		-	Contains the Test Data

	Folder : Eng2Hin

		Eng2Hin.py 			-	Contains the Transliterate code (English to Hindi)
		EngHinInput.txt		-	Contains the Input Data
		EngHinOutput.txt	-	Contains the Test Data

How to run:
			run python3 Eng2Tam.py (for English to Tamil)
			run python3 Eng2Hin.py (for English to Hindi)

			Both will print the accuracy of each model.



	


































