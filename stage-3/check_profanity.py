import urllib

def read_text():
	quotes = open("./movie_quotes.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text):
	con = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
	output = con.read()
	#print(output)
	con.close()
	if "true" in output:
		print("Profanity Alert!")
	elif "false" in output:
		print("This document has no curse words")
	else:
		print("Could not scan the document properly.")

read_text()