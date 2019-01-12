### Created on 29-12-2017
### @author: nad.

# Count the words
def count_words(s):
	num_of_words = len(s.split())
	return num_of_words

# Display the number of words in the text the user typed
def count_words_text(text):
    print(count_words(text), 'words\n')

# Display the number of words in the file
def count_words_file(the_file):
    file = open(the_file, 'r', encoding='utf-8')
    text = file.read()
    print(count_words(text), 'words\n')
    
while True:
    selected = input('Choose: type text or from file? (blank to quit)\n')

    # Stop the program
    if selected == '':
        break

    if selected == 'type text':
        input_text = input('\nType text:\n')
        count_words_text(input_text)

    if selected == 'from file':
        insert_file = input('\nInsert file:\n')
        count_words_file(insert_file)
