### Created on 29-12-2017
### @author: nad.

# Count the words
def count_words(s):
	num_of_words = len(s.split())
    return num_of_words

# Count the words in the file
def count_words_file(the_file):
    file = open(the_file, 'r', encoding='utf-8')
    text = file.read()
    return count_words(text)

# Display the number of words
def display_num_of_words(n):
    print(n, 'words\n')
    
while True:
    selected = input('Enter type text or from file (blank to quit):\n')

    # Stop the program
    if selected == '':
        break

    if selected == 'type text':
        input_text = input('\nType text:\n')
        display_num_of_words(count_words(input_text))

    if selected == 'from file':
        insert_file = input('\nInsert file:\n')
        display_num_of_words(count_words_file(insert_file))
