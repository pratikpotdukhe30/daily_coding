# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num_of_shoes = int(input())

shoes_available_in_shop = list(map(int, input().split()))

total_money_earn = 0
num_of_customers = int(input())

while num_of_customers > 0:
    size, price = input().split()
    if int(size) in Counter(shoes_available_in_shop).keys():
         total_money_earn += int(price)
         shoes_available_in_shop.remove(int(size))
    num_of_customers -= 1


#print(shoes_available_in_shop) 
#print(Counter(shoes_available_in_shop))   
#print(Counter(shoes_available_in_shop).items())
#print(Counter(shoes_available_in_shop).keys())
#print(Counter(shoes_available_in_shop).values())  
print(total_money_earn)  
