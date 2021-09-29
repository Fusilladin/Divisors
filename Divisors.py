# Divisors

while True:
    try:
        num_1 = (str(input("Pick a number.  ")))
        num_str = num_1.split(" ")[0]
        num_2 = int(float(num_str))
    except ValueError:
        print("\nERROR; please type a number!")
        continue
    else:
        print("\nYour number is '{}'.".format (num_2))
        break

a = [*range(1, (num_2 + 1), 1)]
b = []

print("The numbers divisible by {} are:".format(num_2))
for elem in a:
    if num_2 % elem == 0:
        print(elem)
#         b.append(elem)
#         continue
#     else:
#         print(b)
#         break




# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
