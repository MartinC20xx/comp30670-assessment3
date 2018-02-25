# revision on how to read from files

# possible reference - https://stackoverflow.com/questions/16870648/python-read-website-data-line-by-line-when-available

import requests

# need to be able to read from local files too

#url = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
# why b and ''? - is bytes type. 
# might be quicker to just get whole file at the beginning.
r = requests.get('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt', stream=True)



for line in r.iter_lines():
    if line: 
        print(type(line))
        str = line.decode("utf-8") # decode converts from bytes type to str
        print(type(str))
        print(str)

print(type(r))
       
    


