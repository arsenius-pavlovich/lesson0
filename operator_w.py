import string

class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = file_names

    def get_all_words(self):

        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:

                    content = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, ' ')

                    all_words[file_name] = content.split()
            except FileNotFoundError:
                print(f"File {file_name} not found.")
                all_words[file_name] = []
        return all_words

    def find(self, word):

        word = word.lower()
        result = {}

        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            try:

                position = words.index(word) + 1
                result[file_name] = position
            except ValueError:

                result[file_name] = None
        return result

    def count(self, word):

        word = word.lower()
        result = {}

        all_words = self.get_all_words()
        for file_name, words in all_words.items():

            count = words.count(word)
            result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


