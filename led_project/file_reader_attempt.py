# revision on how to read from files

# possible reference - https://stackoverflow.com/questions/16870648/python-read-website-data-line-by-line-when-available

import requests


#url = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'


# have an if statement check for local file or online (if starts with http:?)

# dummy input
global instructions_text  # temporarily using global var. won't need when methods are set up
input = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'

if(input.startswith('http://')):
    r = requests.get('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt', stream=True)
    instructions_text = r.text
else:
    instructions_text = input
    
instructions_list = instructions_text.split(sep='\n')

for instruction in instructions_list:
    
    if('turn on' in instruction):
        pass
    elif('turn off' in instruction):
        pass
    elif('switch' in instruction):
        pass
    
    print(instruction)




       
    


