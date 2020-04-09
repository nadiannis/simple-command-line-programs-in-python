### Created on 26-04-2019

while True:
    text = input('Enter a text (blank to stop): ').lower()
    rev_text = text[::-1]

    if text == '':
        break 
    elif text == rev_text:
        print('It is palindrome.\n')
    else:
        print('It is not palindrome.\n')
