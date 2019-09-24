import sys


def is_text(sen):
	for letter in sen:
		if not letter.isalpha():
			if not letter.isspace():
				if letter != "," and letter != "." and letter != "!" and letter != "?":
					return False
	return True


def repr(array):
	for element in sorted(array):
		print(element)
	return


def main():
	sentence = str(input("Enter a sentence: "))
	sen_is_text = is_text(sentence)
	if sen_is_text:
		array_of_words = sentence.split()
		for i in range(len(array_of_words)):
			word = array_of_words.pop(0).capitalize()
			array_of_words.append(word)
		repr(array_of_words)
		sys.exit(0)
	else:
		print('Please, enter a sentence consists only words!')


if __name__ == '__main__':
	while True:
		main()
