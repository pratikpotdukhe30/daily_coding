# Enter your code here. Read input from STDIN. Print output to STDOUT

mydict = {}

i = int(input())

while(i>0):
    string, price = input().rsplit(' ', 1)
    if string not in mydict:
        mydict[string] = 0
    mydict[string] += int(price)    
    i-=1

for key, value in mydict.items():
    print(key, value)


    
