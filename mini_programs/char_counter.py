### Created on 11-1-2019
### @author: nad

while True:
    print('\nEnter text (blank to quit): ')
    text = input()
    
    # Stop the program
    if text == '':
        break

    count = {}
    for char in text:
        # count.setdefault(char, 0)
        if char not in count:
            count[char] = 0

        count[char] = count[char] + 1
    
    # Display the result
    for k, v in count.items():
        if v == 1:
            print(k + ': ' + str(v) + ' character')
        else:
            print(k + ': ' + str(v) + ' characters')
