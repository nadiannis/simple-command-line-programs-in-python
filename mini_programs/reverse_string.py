### Created on 28-12-2017
### @author: nad.

def reverse_string(string):
        return string[::-1]
	
while True:
    text = input('Type text (blank to quit): ')
	
    # Stop the program
    if text == '':   
        break
		
    print(reverse_string(text) + '\n')
