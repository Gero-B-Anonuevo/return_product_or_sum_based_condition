# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

#pseudocode
#ask input
first_number = int(input("Input the first number: "))
second_number = int(input("Input your second number: "))
#get product
if (first_number*second_number) <= 1000:
    print(first_number*second_number)
else:
    print( int(first_number) + int(second_number)) 
#if product=<1000
#else return sum

