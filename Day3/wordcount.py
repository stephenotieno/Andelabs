def words(sentence):
	wordlist = sentence.split()
	wordfrequency = [wordlist.count(w) for w in wordlist]
	return dict(zip(wordlist, wordfrequency))

