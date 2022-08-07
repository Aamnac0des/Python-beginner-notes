# ARTHMETIC OPERATIONS --
# addition:  3 + 2
# subt:      3 - 2
# multp:     3 * 2
# divisiom:  3 / 2
# floor div: 3 //2
# exponent:  3 ** 2
# modulus:   3 % 2

#COMPARISONS --
# equal: 3 == 2
# not equal: 3 != 2
# greater than: 3 > 2
# less than: 3 < 2
# greater or equal: 3 >= 2
# less or equal: 3 <= 2

# python3 follows order of operations:
print(3 * 2 + 1)
print(3 * (2 + 1))

# incrementing a variable --
num = 1
num += 1 #same as (num = num + 1)
print(num)

print(abs(-3))  #absolute value of a number
print(round(3.75))
print(round(3.75, 1))  #means we want to round to first digit after decimal)


num_1 = 3
num_2 = 2
print(num_1 == num_2)  #returns true/false
print(num_1 >= num_2)

# CASTING --
num_1 = '100'
num_2 = '200'
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
