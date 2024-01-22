# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.



first_number = int(input("Input the first number: "))
second_number = int(input("Input your second number: "))

if (first_number*second_number) <= 1000:
    print(first_number*second_number)
else:
    print( int(first_number) + int(second_number)) 

#def multiplication_or_sum(num1, num2):
    # calculate product of two number
#    product = num1 * num2
    # check if product is less then 1000
#    if product <= 1000:
#        return product
#   else:
        # product is greater than 1000 calculate sum
#        return num1 + num2

#esult = multiplication_or_sum(first_number , second_number)
#rint("The result is", result)