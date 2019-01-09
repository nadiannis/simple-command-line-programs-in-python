### Created on 29-12-2017
### @author: nad

while True:
    print('[Type -stop- to stop the program.]')
    selected = str(input('Choose: type text or from file? '))

    if selected == '-stop-':
        break

    if selected == 'type text':
        text = str(input('\nType text:\n'))

        def count_words(string):
            number_of_words = len(string.split())
            print(str(number_of_words), 'words\n')

        count_words(text)

    if selected == 'from file':
        insert_file = str(input('\nInsert file:\n'))

        def count_words_from_file(the_file):
            file = open(the_file, 'r', encoding='utf-8')
            text = file.read()
            number_of_words = len(text.split())
            print(str(number_of_words), 'words\n')

        count_words_from_file(insert_file)
