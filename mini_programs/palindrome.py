### Created on 26-04-2019
### @author: annadineyl

while True:
    text = input('Enter a text (blank to stop): ')
    rev_text = text[::-1]

    if text == '':
        break 
    elif text.lower() == rev_text.lower():
        print('It is palindrome.\n')
    else:
        print('It is not palindrome.\n')
