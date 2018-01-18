#Maia Reynolds
#1/17/18
#stringAnalysis.py - number of words and characters in a sentence, searching for words and characters

sentence=input("Enter a sentence: ")
characters=len(sentence)
spaces=int((sentence.count(" ")))
periods=int((sentence.count(".")))
questionMarks=int((sentence.count("?")))
commas=int((sentence.count(",")))
dashes=int((sentence.count("-")))
apostrophes=int((sentence.count("'")))
semicolons=int((sentence.count(";")))
colons=int((sentence.count(":")))
exMark=int((sentence.count("!")))
letters=int(characters-(spaces+periods+questionMarks+commas+dashes+apostrophes+semicolons+colons+exMark))
print("Your sentence has ",spaces+1,"words and ",characters,"characters and ",letters,"letters")