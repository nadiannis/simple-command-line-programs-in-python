### Created on 29-12-2017

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
    selected = input('Enter type text or from file (blank to quit):\n').lower()

    if selected == '':
        break  # Stop the program
    elif selected == 'type text':
        text = input('\nType text (type * to go back):\n')
        if (text == '*'):
            continue;
        else:
            display_num_of_words(count_words(text))
    elif selected == 'from file':
        file = input('\nInsert file (type * to go back):\n')
        if (file == '*'):
            continue;
        else:
            display_num_of_words(count_words(text))
    else:
        print('Invalid input.\n')