### Created on 28-12-2017
### @author: nad

while True:
    print('[Type -stop- to stop the program.]')
    text = str(input('Type text: '))

    if text == '-stop-':   #stop the program
        break

    def reverse_string(string):
        return string[::-1]

    print(reverse_string(text) + '\n')
