### Created on 29-12-2017

# Count the words
def count_words(s):
    num_of_words = len(s.split())
    return num_of_words

# Count the words in the file
def count_words_file(filepath):
    file = open(filepath, 'rt', encoding='utf-8')
    lines = (line.strip() for line in file)  # Using generator comprehension is memory
    total = 0                                # efficient while dealing with large files
    for line in lines:
        total += count_words(line)
    file.close()
    return total


while True:
    selected = input('''\nEnter type:
    t: for text
    f: for file
    [blank to quit] => ''').lower()
    
    if selected == '':
        break  # Stop the program
    elif selected == 't':
        text = input('\nEnter Text [ * to go back]: ')
        if text == '*':
            continue
        else:
            n = count_words(text)
            print(n, 'words')
    elif selected == 'f':
        filepath = input('\nEnter Filepath [ * to go back]: ')
        if filepath == '*':
            continue
        else:
            n = count_words_file(filepath)
            print(n, 'words')
    else:
        print('Invalid input.')
