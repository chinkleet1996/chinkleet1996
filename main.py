# below uses the indexing in which we can get the position of a specific character in our string
print("Hello\n"[4])

# below code indicates that anthing inside the double qoutes will be treated as string in python
print("123"+"456\n")

# now below code used integer data type that sum up two integer numbers
print(123 + 456)

#Float data type
3.154

#Boolean
True
False

num_char = len(input("What is your class name? "))

# str method can be used to chnage the data type
new_num_char = str(num_char)
print("your name has " + new_num_char + " number of characters.\n")

# type method to use in case of no idea of the data type
print(type(num_char))



# below are some examples for data type changing / type casting method

a = float(1298)
print(a)

print(70 + float(1250))
print("\n")


# below code first takes the input from the user
# then pick out the 0th and 1st index digits
# then convert the string value to the equivalent int data type
# finally perform the addition between the numbers.
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))
print("\n")

# below is the example of different operator and their working preecedence
# computation always from the left to right side
# so first it will multiply (4 * 4) = 16
# then comes to the div part (4 / 4) = 1.0
# then comes to add part 16 + 1.0 = 17.0
# finally sub comes into the picture 17.0 - 4 = 13.0
print( 4 * 4 + 4 / 4 - 4)



# below code shows the working of a BMI calculater which takes height and weight as an input and shows BMI value.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = int(weight) / float(height) ** 2
print(int(BMI))