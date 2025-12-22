import textwrap

def wrap(string, max_width):
    
    return textwrap.fill(string, max_width) 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#Same code without textwrap library and own logic -

import textwrap

def wrap(string, max_width):
    finalStr = ""
    for i in range(0, len(string), max_width):
        finalStr += string[i:i+max_width] + "\n"
    
    return finalStr
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
