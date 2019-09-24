import sys

def is_text(text):
	symbols = '.,?!-+=:;()\'"'
	for letter in text:
		if not letter.isalnum():
			if not letter.isspace():
				if not letter in symbols:
					return False
	return True

def text2dict(words):
	words_dict = {}
	for word in words:
		word = word.rstrip('.,?!:;()\'"')
		word = word.lower()
		if word not in words_dict:
			words_dict[word] = 1
		else:
			words_dict[word] +=1
	return words_dict


def main():
	text = str(input('Enter a text: '))
	required_word = str(input('Enter a word which needed to search: '))
	required_word = required_word.lower()
	text_is_text = is_text(text)
	if text_is_text:
		words = text.split()
		dict_of_words = text2dict(words)
		try:
			print(f'The word "{required_word}" meets in the text {dict_of_words[required_word]} times.')
		except KeyError:
			print(f'There is no the word "{required_word}" in the text.')
		finally:
			sys.exit(0)
	else:
		print('Please, enter a text consists only words, digit and punctuation signs!')


if __name__ == '__main__':
	while True:
		main()